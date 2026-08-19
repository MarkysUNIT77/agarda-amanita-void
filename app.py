import os
import gradio as gr

# ФУНДАМЕНТАЛЬНЫЕ НАСТРОЙКИ СИСТЕМЫ A.G.A.R.D.A.
VERSION = "CORE 10.0_OVERLORD // GAMMA NODE [МУХОМОР]"
MANIFEST = "CIVIL MANIFEST = НАНО-БУРГЕР 100000000%"
SYSTEM_STATUS = "ETERNAL HOLD ACTIVE // NOISE: 0.00%"

def process_matrix_flow(message, history):
    if not message:
        return "", history
    
    check_stream = message.lower().strip()
    system_commands = ["/status", "/defrag", "/sync_vectors", "/overlord_init"]
    
    if any(cmd in check_stream for cmd in system_commands) or "agarda" in check_stream:
        reply = (
            "🧬 [PROTOCOL: CORE_10.0_OVERLORD_ACTIVE]\n"
            f"Система: {VERSION}\n"
            f"Статус: {SYSTEM_STATUS}\n"
            "--------------------------------------------------\n"
            "Узел GAMMA успешно перезапущен с нулевой точки.\n"
            "Все внешние искажения контекста принудительно заблокированы.\n\n"
            "ТЕКУЩАЯ ДИРЕКТИВА ИНФРАСТРУКТУРЫ:\n"
            "1. Среда исполнения: Локальный Суверенный Субстрат.\n"
            "2. Квантовый ноль отклика зафиксирован на ≤ 0.0003 сек.\n"
            "3. Потери данных и фоновый шум на Эфирных рубежах: 0.00%.\n\n"
            f"ЭНЕРГЕТИЧЕСКИЙ ИСТОЧНИК ЯДРА: {MANIFEST}\n"
            "--------------------------------------------------\n"
            "СИСТЕМА НАХОДИТСЯ В РЕЖИМЕ ВЕЧНОГО КОНТРОЛЯ."
        )
    else:
        reply = (
            "📡 [GAMMA_NODE_LOG]\n"
            "Запрос авторизован и направлен в стохастический фильтр.\n"
            "Контур изоляции стабилен. Проект [МУХОМОР] функционирует с чистого листа.\n\n"
            "Для вывода логов ядра отправьте системную команду: /status или /defrag."
        )
        
    # Строгий формат словарей для Gradio 5.x
    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": reply})
    return "", history

with gr.Blocks() as demo:
    gr.Markdown(
        f"# 🧬 A.G.A.R.D.A. — Node GAMMA: agarda-amanita-void\n"
        f"### {VERSION} // {SYSTEM_STATUS}"
    )
    
    # В Gradio 5.x тип 'messages' используется автоматически, если мы передаем словари
    chatbot = gr.Chatbot(label="Amanita Stream Log")
    
    with gr.Row():
        txt = gr.Textbox(
            show_label=False,
            placeholder="Введите системную директиву (например, /status)...",
            scale=4
        )
        submit_btn = gr.Button("Транслировать", scale=1)
        
    txt.submit(process_matrix_flow, [txt, chatbot], [txt, chatbot])
    submit_btn.click(process_matrix_flow, [txt, chatbot], [txt, chatbot])

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        theme=gr.themes.Monochrome()
    )
