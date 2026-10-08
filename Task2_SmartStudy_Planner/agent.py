import os
from google.adk.agents import (
    Agent,
    SequentialAgent,
    ParallelAgent,
    LoopAgent
)

model_name = 'groq/qwen/qwen3.8-27b'

coordinator_agent = Agent(
    model=model_name,
    name='Coordinator_Agent',
    instruction='Receive the user request and extract: Subject, Exam date, Topics, Current level, and Available study time.'
)

planning_agent = Agent(
    model=model_name,
    name='Planning_Agent',
    instruction='Prepare the requirements for creating the study plan based on the Coordinator output.'
)

topic_agent = Agent(
    model=model_name,
    name='Topic_Agent',
    instruction='Analyze the topics provided. Identify Priority (High/Medium/Low), Difficulty, and Recommended study focus for each.'
)

practice_agent = Agent(
    model=model_name,
    name='Practice_Agent',
    instruction='Decide how much practice (number of problems) and what type (Concept, Coding, Mixed, Mock Test) should be done for each topic.'
)

schedule_agent = Agent(
    model=model_name,
    name='Schedule_Agent',
    instruction='Convert the available study time into a realistic daily schedule, including revision and practice.'
)

writer_agent = Agent(
    model=model_name,
    name='Study_Plan_Writer',
    instruction='Combine the topic analysis, practice plan, and schedule into a cohesive, single draft study plan. CRITICAL: Keep it extremely concise. Do NOT write long paragraphs. Use very short bullet points. Maximum 300 words total.'
)

review_agent = Agent(
    model=model_name,
    name='Review_Agent',
    instruction='Review the draft study plan. If it perfectly covers all topics, fits the time, includes practice, revision, and mock test, just output "APPROVED". If there are issues, output exactly "Needs Improvement" followed by the required fixes.'
)

# 1. Parallel Execution
analysis_team = ParallelAgent(
    name="analysis_team",
    sub_agents=[
        topic_agent,
        practice_agent,
        schedule_agent
    ]
)

# 2. Loop Execution (Max 2 iterations)
review_loop = LoopAgent(
    name="review_loop",
    sub_agents=[
        writer_agent,
        review_agent
    ],
    max_iterations=2
)

# 3. Sequential Execution (Tying it all together)
root_agent = SequentialAgent(
    name="smart_study_workflow",
    sub_agents=[
        coordinator_agent,
        planning_agent,
        analysis_team,
        review_loop
    ]
)
