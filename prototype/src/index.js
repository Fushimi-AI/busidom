#!/usr/bin/env node

/**
 * Business-OS CLI
 * 48-hour prototype - just the essentials
 * 
 * Usage:
 *   bos              - Start chat with mentor
 *   bos --clear      - Clear conversation history
 *   bos --help       - Show help
 */

const readline = require('readline');
const { MENTOR_SYSTEM_PROMPT, CONTEXT_TEMPLATE } = require('./mentor-prompt');
const { loadContext, saveContext, addToHistory, formatHistoryForPrompt, clearContext } = require('./context');

// Check for API key
const API_KEY = process.env.KIMI_API_KEY || process.env.OPENAI_API_KEY;
const API_BASE = process.env.KIMI_API_BASE || 'https://api.openai.com/v1';
const MODEL = process.env.BOS_MODEL || 'gpt-4'; // Default to GPT-4, can switch to Kimi

if (!API_KEY) {
  console.log('\n⚠️  No API key found.\n');
  console.log('Set one of these environment variables:');
  console.log('  export KIMI_API_KEY=your-key-here    # For Kimi K2.5');
  console.log('  export OPENAI_API_KEY=your-key-here  # For OpenAI\n');
  console.log('Optional:');
  console.log('  export KIMI_API_BASE=https://api.moonshot.ai/v1  # Kimi endpoint');
  console.log('  export BOS_MODEL=kimi-k2.5                       # Model name\n');
  process.exit(1);
}

// Handle command line args
const args = process.argv.slice(2);
if (args.includes('--help') || args.includes('-h')) {
  console.log(`
Business-OS - AI Mentor for Entrepreneurs

Usage:
  bos              Start conversation with your AI mentor
  bos --clear      Clear conversation history and start fresh
  bos --help       Show this help message

Commands during chat:
  /clear           Clear history
  /context         Show current context
  /quit or /exit   Exit the chat

Environment variables:
  KIMI_API_KEY     API key for Kimi (recommended - 6x cheaper)
  OPENAI_API_KEY   API key for OpenAI (fallback)
  KIMI_API_BASE    API endpoint (default: OpenAI compatible)
  BOS_MODEL        Model to use (default: gpt-4)
`);
  process.exit(0);
}

if (args.includes('--clear')) {
  clearContext();
  console.log('✓ Conversation history cleared.\n');
  process.exit(0);
}

// Initialize
let context = loadContext();

// Simple API call function (OpenAI compatible)
async function callAI(messages) {
  const response = await fetch(`${API_BASE}/chat/completions`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${API_KEY}`
    },
    body: JSON.stringify({
      model: MODEL,
      messages: messages,
      max_tokens: 1000,
      temperature: 0.8
    })
  });

  if (!response.ok) {
    const error = await response.text();
    throw new Error(`API Error: ${response.status} - ${error}`);
  }

  const data = await response.json();
  return data.choices[0].message.content;
}

// Build messages array for API
function buildMessages(userMessage, context) {
  const historyText = formatHistoryForPrompt(context.history);
  
  let systemContent = MENTOR_SYSTEM_PROMPT;
  
  // Add context if we have business info
  if (context.business_name) {
    systemContent += `\n\n## Current Business Context\nBusiness: ${context.business_name}\nStage: ${context.stage}`;
    if (context.challenge) {
      systemContent += `\nCurrent Challenge: ${context.challenge}`;
    }
  }
  
  // Add recent history summary
  if (context.history.length > 0) {
    systemContent += `\n\n## Recent Conversation\n${historyText}`;
  }

  return [
    { role: 'system', content: systemContent },
    { role: 'user', content: userMessage }
  ];
}

// Handle special commands
function handleCommand(input, context) {
  const cmd = input.trim().toLowerCase();
  
  if (cmd === '/clear') {
    context = clearContext();
    console.log('\n✓ History cleared. Fresh start.\n');
    return { handled: true, context };
  }
  
  if (cmd === '/context') {
    console.log('\n--- Current Context ---');
    console.log(`Business: ${context.business_name || 'Not set'}`);
    console.log(`Stage: ${context.stage}`);
    console.log(`Challenge: ${context.challenge || 'Not set'}`);
    console.log(`Messages: ${context.history.length}`);
    console.log('----------------------\n');
    return { handled: true, context };
  }
  
  if (cmd === '/quit' || cmd === '/exit') {
    console.log('\nSee you next time. Now go build something.\n');
    process.exit(0);
  }
  
  return { handled: false, context };
}

// Extract business info from conversation
function extractBusinessInfo(userMessage, aiResponse, context) {
  // Simple extraction - can be improved later
  const lowerMsg = userMessage.toLowerCase();
  
  // Try to extract business name if mentioned
  const nameMatch = userMessage.match(/(?:called|named|it's|building)\s+["']?([A-Z][a-zA-Z0-9\s]+?)["']?(?:\s|,|\.|\?|$)/i);
  if (nameMatch && !context.business_name) {
    context.business_name = nameMatch[1].trim();
  }
  
  return context;
}

// Main chat loop
async function main() {
  console.log(`
╔═══════════════════════════════════════════════════════════════╗
║                      BUSINESS-OS                               ║
║              Your AI Co-Founder                                ║
╚═══════════════════════════════════════════════════════════════╝

${context.business_name ? `Working on: ${context.business_name}` : 'New session - tell me about your business.'}

Type your message. Commands: /clear /context /quit
─────────────────────────────────────────────────────────────────
`);

  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
  });

  const prompt = () => {
    rl.question('\n📝 You: ', async (input) => {
      if (!input || !input.trim()) {
        prompt();
        return;
      }

      // Handle commands
      const cmdResult = handleCommand(input, context);
      if (cmdResult.handled) {
        context = cmdResult.context;
        prompt();
        return;
      }

      try {
        process.stdout.write('\n🧠 Mentor: ');
        
        const messages = buildMessages(input, context);
        const response = await callAI(messages);
        
        console.log(response);
        
        // Update context
        context = addToHistory(context, 'user', input);
        context = addToHistory(context, 'assistant', response);
        context = extractBusinessInfo(input, response, context);
        saveContext(context);
        
      } catch (error) {
        console.log(`\n❌ Error: ${error.message}`);
        console.log('Check your API key and try again.\n');
      }

      prompt();
    });
  };

  prompt();

  rl.on('close', () => {
    console.log('\n\nSession saved. Now go build something.\n');
    process.exit(0);
  });
}

main();
