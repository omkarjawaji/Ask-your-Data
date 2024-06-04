import os
import pandas as pd
from pandasai import Agent
from dotenv import load_dotenv

load_dotenv()


class DataAnalyzer:
    def __init__(self, df):
        self.agent = Agent(df)
        os.environ["PANDASAI_API_KEY"] = os.getenv("PANDASAI_API_KEY")

    def interpret_question(self, query):
        response = self.agent.chat(query)
        return response




