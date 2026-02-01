/**
 * Simple Context Management
 * Save and load conversation to JSON file
 */

const fs = require('fs');
const path = require('path');

const CONTEXT_FILE = path.join(process.env.HOME || process.env.USERPROFILE, '.business-os-context.json');

const DEFAULT_CONTEXT = {
  business_name: null,
  stage: 'ideation',
  challenge: null,
  history: [],
  created_at: new Date().toISOString(),
  updated_at: new Date().toISOString()
};

function loadContext() {
  try {
    if (fs.existsSync(CONTEXT_FILE)) {
      const data = fs.readFileSync(CONTEXT_FILE, 'utf8');
      return JSON.parse(data);
    }
  } catch (error) {
    console.error('Error loading context, starting fresh:', error.message);
  }
  return { ...DEFAULT_CONTEXT };
}

function saveContext(context) {
  try {
    context.updated_at = new Date().toISOString();
    fs.writeFileSync(CONTEXT_FILE, JSON.stringify(context, null, 2));
  } catch (error) {
    console.error('Error saving context:', error.message);
  }
}

function addToHistory(context, role, content) {
  // Keep last 20 messages to manage token limits
  context.history.push({ role, content, timestamp: new Date().toISOString() });
  if (context.history.length > 40) {
    context.history = context.history.slice(-40);
  }
  return context;
}

function formatHistoryForPrompt(history) {
  if (!history || history.length === 0) return 'No previous conversation.';
  
  return history
    .slice(-10) // Last 10 exchanges for context
    .map(msg => `${msg.role === 'user' ? 'User' : 'Mentor'}: ${msg.content}`)
    .join('\n\n');
}

function clearContext() {
  saveContext({ ...DEFAULT_CONTEXT });
  return { ...DEFAULT_CONTEXT };
}

module.exports = {
  loadContext,
  saveContext,
  addToHistory,
  formatHistoryForPrompt,
  clearContext,
  CONTEXT_FILE
};
