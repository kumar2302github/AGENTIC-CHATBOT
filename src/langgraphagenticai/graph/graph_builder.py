from langgraph.graph import StateGraph
from src.langgraphagenticai.state.state import State
from langgraph.graph import START, END
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
    
    def basic_chatbot_build_graph(self):
        """
        Build a basic chatbot graph with the provided LLM.
        This method in slices a chat bot node using the basic chat bot node class and integrate it into the graph. The chatbot node is set as both the entry and exit point of the graph.
        """

        self.basic_chatbot_node = BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot", END)

    def setup_graph(self,usecase: str):
        """
        Setup the graph with the basic chatbot node.
        This method is called to initialize the graph with the basic chatbot node.
        """
        if usecase != "Basic Chatbot":
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()