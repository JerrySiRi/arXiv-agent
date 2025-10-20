# 🚀 arXiv-daily 

This innovative tool transforms how you stay updated with arXiv papers by combining automated crawling with AI-powered summarization. Amended from https://dw-dengwei.github.io/daily-arXiv-ai-enhanced/. Thanks for all developers!


## ✨ Key Features

**[Try it now!](https://jerrysiri.github.io/arXiv-agent/)** - No installation required

 **Zero Infrastructure Required**
- Leverages GitHub Actions and Pages - no server needed
- Completely free to deploy and use

 **Smart AI Summarization**
- Daily paper crawling with DeepSeek-powered summaries
- Cost-effective: Only ~0.2 CNY per day
- After the analysis is completed, an email will be sent to inform (need your config)

**Smart Reading Experience**
- Personalized paper highlighting based on your interests
- Cross-device compatibility (desktop & mobile)
- Local preference storage for privacy
- Flexible date range filtering



# How to use
This repo will daily crawl arXiv papers about **cs.CV, cs.GR, cs.CL and cs.AI**, and use **DeepSeek** to summarize the papers in **Chinese**.
If you wish to crawl other arXiv categories, use other LLMs, or other languages, please follow the instructions.
Otherwise, you can directly use this repo in https://jerrysiri.github.io/arXiv-agent/. Please star it if you like :)

**Instructions:**
1. Fork this repo to your own account
2. Go to: your-own-repo -> Settings -> Secrets and variables -> Actions
3. Go to Secrets. Secrets are encrypted and used for sensitive data
4. Create two repository secrets named `OPENAI_API_KEY` and `OPENAI_BASE_URL`, and input corresponding values.
5. Go to Variables. Variables are shown as plain text and are used for non-sensitive data
6. Create the following repository variables:
   1. `CATEGORIES`: separate the categories with ",", such as "cs.CL, cs.CV"
   2. `LANGUAGE`: such as "Chinese" or "English"
   3. `MODEL_NAME`: such as "deepseek-chat"
   4. `EMAIL`: your email for push to GitHub
   5. `NAME`: your name for push to GitHub
7. Go to your-own-repo -> Actions -> arXiv-daily-ai-enhanced
8. You can manually click **Run workflow** to test if it works well (it may take about one hour). By default, this action will automatically run every day. You can modify it in `.github/workflows/run.yml`
9.  Set up GitHub pages: Go to your own repo -> Settings -> Pages. In `Build and deployment`, set `Source="Deploy from a branch"`, `Branch="main", "/(root)"`. Wait for a few minutes, go to https://\<username\>.github.io/daily-arXiv-ai-enhanced/. Please see this [issue](https://github.com/dw-dengwei/daily-arXiv-ai-enhanced/issues/14) for more precise instructions.

# Plans

Customized Plan:
- Bug to be fixed: Web Spider is missing articles...
- Images related to summary
- Email function
- Filtered (or ranked) by relevance
- Interface from OpenReview (get instant feedback from reviewer's feedback for each paper)

See original project page: https://github.com/users/dw-dengwei/projects/3
