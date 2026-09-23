# Drive report

Base: http://127.0.0.1:4321
Fails: 0 / 35

| Step | Expected | Observed | Result |
|---|---|---|---|
| home h1 | LLM Knowledge Base | LLM Knowledge Base | pass |
| home doors | 5 Understand Apply Learn Decode Explore | 5 Understand Apply Learn Decode Explore | pass |
| explore href | /map/ | /map/ | pass |
| top of mind | 4 | 4 | pass |
| home graph mode | spine | spine | pass |
| home nav on | none | none | pass |
| map url | /map or /map/ | /map/ | pass |
| map h1 | The vault | The vault | pass |
| map nav | Map | Map | pass |
| map graph | full + domain labels + canvas | full labels=true canvas=true unavailable=false | pass |
| domain url | /domains/learning/ | /domains/learning/ | pass |
| domain h1 | includes Learning | Learning | pass |
| domain moc | >=1 | 132 | pass |
| domain nav | Notes | Notes | pass |
| understand url | /wiki/Concepts/The-AI-Industrial-Revolution/ | /wiki/Concepts/The-AI-Industrial-Revolution/ | pass |
| understand h1 | The AI Industrial Revolution | The AI Industrial Revolution | pass |
| understand dek | absent | false | pass |
| understand type | Concept | Concept | pass |
| understand crumb | wiki → /folder/wiki/ | wiki /folder/wiki/ | pass |
| understand related fold | N more related pages | 10 more related pages | pass |
| understand local graph | local | local | pass |
| prose link found | Agentic Engineering, Condensed | Agentic Engineering, Condensed | pass |
| prose land h1 | Agentic Engineering, Condensed | Agentic Engineering, Condensed @ /wiki/Systems/AI--and--Agentic-Systems/Agentic-Engineering,-Condensed/ | pass |
| notes url | /notes/ | /notes | pass |
| notes nav | Notes | Notes | pass |
| notes heads | Condensed, Hubs | Condensed, Hubs | pass |
| notes rows | >=1 | 17 | pass |
| notes graph | full | full | pass |
| notes omits extra hubs | no Using Grok Bot / pstack / Cursor Cloud Agents / Picking a computer | none of those four | pass |
| condensed h1 | Learning, Condensed | Learning, Condensed | pass |
| condensed dek | starts The whole learning corpus | The whole learning corpus stated as rules: one rule per line, and each line link | pass |
| condensed type | Condensed | Condensed | pass |
| condensed crumb | /folder/wiki/ | /folder/wiki/ | pass |
| search open | rows for Vibe Coding | 8 first=Vibe Coding | pass |
| search land | Vibe Coding | Vibe Coding @ /wiki/Systems/AI--and--Agentic-Systems/Vibe-Coding/ | pass |
