import os
from typing import List
from dotenv import load_dotenv
from langchain_groq import chatgroq
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, field, validator
