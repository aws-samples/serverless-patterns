from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from datetime import datetime
from strands import Agent
import random

app = FastAPI(title="Fraud Detection Agent", version="1.0.0")

# Initialize Strands agent
strands_agent = Agent()

class InvocationRequest(BaseModel):
    input: Dict[str, Any]

class InvocationResponse(BaseModel):
    output: Dict[str, Any]


"""
Fraud risk scoring agent 

Returns a risk score between 1-5 based on transaction amount:
- For amounts <= 10000: Returns 1-5 with weighted distribution (60% chance of 2)
- For amounts > 10000: Returns 3-5 only with weighted distribution

Weighting:
- Score 2 appears ~60% of the time (when applicable)
- Score 3 appears ~25% of the time
- Other scores split the remaining probability
"""

@app.post("/invocations", response_model=InvocationResponse)
async def invoke_agent(request: InvocationRequest):
    try:
        # RETRIENVE THE FULL JSON INPUT OBJECT AS A DICT
        input_data = request.input
        amount = input_data.get("amount", "")
        if not amount:
            raise HTTPException(status_code=400, detail="Amount not provided, please provide the 'amount' in USD")

        #IF WE WANTED TO SEND TO THE AGENT, WE WOULD INVOKE THE STRANDS_AGENT. FOR SIMPLCITY, WE'RE JUST USING RULE-BASED SCORING
        #result = strands_agent(amount)
         
        # Determine risk score based on amount
        if amount < 1000:
            # Low amount: auto-approve (score 1-2)
            risk_score = random.choices(
                population=[1, 2],
                weights=[60, 40],
                k=1
            )[0]
        elif amount >= 10000:
            # Very high amount: always send to fraud (score 5)
            risk_score = 5
        elif amount == 6500:
            # Specific test case: medium risk requiring human verification
            risk_score = 3
        elif amount >= 5000:
            # High amount: return 3-5
            # Weight: 3 (~50%), 4 (~30%), 5 (~20%)
            risk_score = random.choices(
                population=[3, 4, 5],
                weights=[50, 30, 20],
                k=1
            )[0]
        else:
            # Normal amount (1000-4999): return 1-4
            # Weight: 2 (~50%), 3 (~30%), 1 (~15%), 4 (~5%)
            risk_score = random.choices(
                population=[1, 2, 3, 4],
                weights=[15, 50, 30, 5],
                k=1
            )[0]
        
        # Return response
        response = {
            'risk_score': risk_score,
            'amount': amount
        }

        return InvocationResponse(output=response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent processing failed: {str(e)}")

@app.get("/ping")
async def ping():
    return {"status": "Fraud agent is running and healthy.  To use, invoke with {amount:x.xx}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)