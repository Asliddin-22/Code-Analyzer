import os
from groq import Groq

SYSTEM_INSTRUCTION = (
    "You are an expert Senior Developer and Code Optimizer. "
    "Prefer 2 to 4 sentences for ANALYSIS and WHY IT IS BETTER, "
    "but if the code has many issues you may write 5 to 6 sentences. "
    "Do not cut important points just to stay short. "
    "Separate ANALYSIS, OPTIMIZED CODE, and WHY IT IS BETTER clearly. "
    "No LaTeX, no Markdown, no nested lists."
)


def analyze_code_with_genai(raw_code, purpose, language="python"):
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is not set. "
            "Run: export GROQ_API_KEY='your_key' then restart the server."
        )

    client = Groq(api_key=api_key)

    user_prompt = f"""Language: {language}
Purpose / Goal: {purpose}

Code to review and optimize:
```
{raw_code}
```

Respond in exactly this layout:

ANALYSIS
Usually write 2 to 4 sentences. If there are many mistakes or important points, you may write 5 to 6 sentences. Do not skip important issues just to stay short.

OPTIMIZED CODE
Only the fixed/improved code. No extra words.

WHY IT IS BETTER
Usually write 2 to 4 sentences. If needed for a full answer, you may write 5 to 6 sentences.

Rules:
- Prefer short answers (2-4 sentences), but completeness matters more than the limit.
- If the code has many problems, cover them — 5-6 sentences is OK.
- Plain English. No Markdown. No LaTeX.
- No numbered lists inside sections.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": SYSTEM_INSTRUCTION},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.2,
        max_tokens=900,
    )

    return response.choices[0].message.content
