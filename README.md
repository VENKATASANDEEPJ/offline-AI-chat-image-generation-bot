# Offline AI Chat + Image Generation Bot

An offline AI assistant that can **chat with users and generate images locally using Stable Diffusion**. This project demonstrates how conversational AI and local text‑to‑image generation can work together without relying on external APIs or cloud services.

---

## 🚀 Features

* 💬 Interactive chatbot interface
* 🎨 Local image generation from text prompts
* 🖥️ Runs completely offline
* ⚡ No external API or internet required after setup
* 🧠 Uses Stable Diffusion for high‑quality image generation

---

## 🧠 Technology Stack

* Python
* PyTorch
* Stable Diffusion
* HuggingFace Diffusers
* Transformers

---

## 📁 Project Structure

```
offline-AI-chat-image-generation-bot
│
├── chatbot.py                # Chatbot interaction logic
├── generate_image.py         # Image generation module
├── image_engine/             # Image generation components
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/VENKATASANDEEPJ/offline-AI-chat-image-generation-bot.git
cd offline-AI-chat-image-generation-bot
```

### 2. Create a virtual environment

```
python -m venv venv
```

Activate the environment.

**Windows**

```
venv\Scripts\activate
```

**Linux / Mac**

```
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## 📥 Download the Stable Diffusion Model

Download the Stable Diffusion model file:

```
v1-5-pruned-emaonly.safetensors
```

Place the downloaded model inside:

```
image_engine/
```

Note: The model is **not included in the repository** because GitHub does not allow very large files. Keeping models separate is standard practice for AI projects.

---

## ▶️ Running the Application

Start the chatbot:

```
python chatbot.py
```

Example prompt:

```
Generate an image of a futuristic city at sunset
```

The generated image will be saved locally in the project directory.

---
sample outputs: 
<img width="512" height="512" alt="output" src="https://github.com/user-attachments/assets/d9617ebf-14e9-4a7f-9cee-a3b068bd332e" />
<img width="512" height="512" alt="output_1769525664" src="https://github.com/user-attachments/assets/a39937bd-1f36-4acb-9931-ee4c6fed4393" />
<img width="512" height="512" alt="output_1769504650" src="https://github.com/user-attachments/assets/6a565597-9767-4d78-86ec-d05c3a023fa7" />


## 🎯 Example Use Cases

* AI creative assistant
* Offline image generation system
* AI experimentation and learning
* Local AI assistant without internet

---

## 🔮 Future Improvements

* Web interface using Flask or Gradio
* Voice input support
* Multiple AI models
* Model auto‑download system
* Chat history support

---

## 👤 Author

**J Venkata Sandeep**

GitHub: [https://github.com/VENKATASANDEEPJ](https://github.com/VENKATASANDEEPJ)

---

## 📜 License

This project is intended for educational and experimental purposes.
