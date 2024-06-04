import os

from pandasai.smart_dataframe import SmartDataframe
from pandasai.llm.openai import OpenAI
from pandasai.schemas.df_config import Config

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


class DataInterpreter:

    def __init__(self, df):
        self.sdf = SmartDataframe(df, config=Config(llm=client))

    def interpret_question(self, query):
        response = self.sdf.chat(query)
        return response
