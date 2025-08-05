from src.langgraphagenticai.state.state import State

class BasicChatbotNode:
    """BASic chatbot implementation"""
    def __init__(self,model):
        self.llm = model

    def process(self, state: State)->dict:
        """
        Process the state and return a response.
        This method is called when the chatbot node is executed in the graph.
        """
        return {"messages":self.llm.invoke(state['messages'])}