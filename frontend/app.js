document.addEventListener('DOMContentLoaded', () => {
    const chatForm = document.getElementById('chat-form');
    const messageInput = document.getElementById('message-input');
    const chatMessages = document.getElementById('chat-messages');

    // Generate a pseudo-random user ID for the session
    const userId = 'user_' + Math.random().toString(36).substring(2, 9);
    
    const suggestionChipsContainer = document.getElementById('suggestion-chips');

    // Pool of diverse questions about Sachin
    const questionPool = [
        "What is your tech stack?",
        "Tell me about your experience.",
        "Where did you go to college?",
        "What did you do at eLoop Dev Solutions?",
        "What did you do at 10Times?",
        "Do you know React and Next.js?",
        "Are you comfortable with Node.js and REST APIs?",
        "Can you build internal admin tools?",
        "What certifications do you hold?",
        "How do you handle UI performance?",
        "Describe your work integrating Gen-AI.",
        "What databases have you worked with?",
        "Why should I hire Sachin?"
    ];

    let unusedQuestions = [...questionPool];
    
    function getRandomQuestions(count) {
        if (unusedQuestions.length < count) {
            unusedQuestions = [...questionPool]; // Refill
        }
        
        // Shuffle current unused array
        for (let i = unusedQuestions.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [unusedQuestions[i], unusedQuestions[j]] = [unusedQuestions[j], unusedQuestions[i]];
        }
        
        // Pop top `count` questions
        return unusedQuestions.splice(0, count);
    }

    function renderChips() {
        suggestionChipsContainer.innerHTML = '';
        const currentQuestions = getRandomQuestions(3); // show 3 at a time
        
        currentQuestions.forEach(q => {
            const btn = document.createElement('button');
            btn.className = 'chip';
            btn.type = 'button';
            btn.textContent = q;
            btn.addEventListener('click', () => {
                messageInput.value = btn.textContent;
                chatForm.dispatchEvent(new Event('submit', { cancelable: true, bubbles: true }));
                // Automatically re-render 3 new question chips instantly
                renderChips();
            });
            suggestionChipsContainer.appendChild(btn);
        });
    }

    // Initial render
    renderChips();

    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const text = messageInput.value.trim();
        if (!text) return;
        
        // 1. Add user message
        addMessage(text, 'user');
        messageInput.value = '';
        
        // 2. Show typing indicator
        const typingId = addTypingIndicator();
        
        // 3. Send request to backend
        try {
            const response = await fetch('/api/v1/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    user_id: userId,
                    message: text
                })
            });
            
            if (!response.ok) throw new Error(`API Error: ${response.status}`);
            
            const data = await response.json();
            
            // 4. Remove typing and add AI response
            removeTypingIndicator(typingId);
            addMessage(data.response, 'ai');
            
        } catch (error) {
            console.error(error);
            removeTypingIndicator(typingId);
            addMessage("Transmission error. Please try again.", 'system-message');
        }
    });
    
    function addMessage(text, sender) {
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ${sender} fade-in`;
        msgDiv.textContent = text;
        
        chatMessages.appendChild(msgDiv);
        scrollToBottom();
    }
    
    function addTypingIndicator() {
        const id = 'typing-' + Date.now();
        const msgDiv = document.createElement('div');
        msgDiv.className = `message ai fade-in`;
        msgDiv.id = id;
        
        msgDiv.innerHTML = `
            <div class="typing-indicator">
                <div class="dot"></div>
                <div class="dot"></div>
                <div class="dot"></div>
            </div>
        `;
        
        chatMessages.appendChild(msgDiv);
        scrollToBottom();
        return id;
    }
    
    function removeTypingIndicator(id) {
        const el = document.getElementById(id);
        if (el) {
            el.remove();
        }
    }
    
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
