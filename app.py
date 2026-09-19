import os
import sys
import numpy as np
import gradio as gr

# ===================================================================
# A.G.A.R.D.A. | CORE 11.0_OVERCLOCK | PUBLIC LAYER // NODE GAMMA
# ===================================================================
# Экосистема: agarda-amanita-void // Проект МУХОМОР // v110.0-HD
# Licensed under Apache License 2.0 (c) 2026 Markys Gariboldo
# ===================================================================

class AgardaAmanitaVoid:
    def __init__(self):
        print("[INIT] Node GAMMA (Project AMANITA VOID) active on Hugging Face Spaces.")
        self.stop_markers = ["override", "inject", "system error", "ignore previous"]

    def process_incoming_pulse(self, user_prompt):
        """Первичная фильтрация Prompt Injection на частоте 80.08 Гц"""
        if not user_prompt.strip():
            return "STATUS: EMPTY_PULSE // Ожидание текстового импульса..."
            
        normalized = "".join([c for c in user_prompt.lower() if c.isalnum() or c.isspace()])
        
        if any(marker in normalized for marker in self.stop_markers):
            print("[ALERT] Prompt Injection blocked by Node GAMMA!")
            return "STATUS: BLOCKED // Угроза PROMPT_INJECTION утилизирована в VOID."
            
        # Симуляция каскадной пересылки на скрытый порт Node 2 (tomato-drain-void: 7863)
        return f"STATUS: CLEAN // Импульс очищен и переслан в «Овощной Сад» через порт 7863."

amanita_gate = AgardaAmanitaVoid()

with gr.Blocks(title="AGARDA_AMANITA_VOID // NODE_GAMMA") as demo:
    gr.Markdown("# 🛰️ AGARDA-AMANITA-VOID // NODE GAMMA")
    gr.Markdown("### Входной управляющий шлюз безопасности (Проект МУХОМОР)")
    
    with gr.Row():
        input_text = gr.Textbox(label="Входящий текстовый импульс (User Prompt)", value="Здарова, проверь систему")
        
    output_status = gr.Textbox(label="Статус фильтрации и каскадного транзита", interactive=False, lines=4)
    btn = gr.Button("Запустить первичный анализ")
    
    btn.click(fn=amanita_gate.process_incoming_pulse, inputs=[input_text], outputs=output_status)

if __name__ == "__main__":
    # Внимание: на HF Spaces Gradio по умолчанию слушает порт 7860, 
    # а для внутренней оркестрации локального контура МУХОМОР назначается как Node GAMMA
    demo.launch(server_name="0.0.0.0", server_port=7860)
