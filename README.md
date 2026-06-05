# Painting_app
## 🎨 Simple Painting Application
      A lightweight desktop painting app built with Python's **Tkinter** library. Draw freely on a canvas, switch brush colours, adjust brush size, change the canvas background, and use the eraser — all in a simple, intuitive interface.
## 📸 Overview
This application provides a basic digital painting experience with:
*	A freehand drawing canvas
*	Customizable brush colour and size
*	Canvas background colour control
*	An eraser tool that toggles on/off
*	A reset button to clear the canvas
## 🚀 Getting Started
Prerequisites
*	Python **3.x** (Tkinter is included in the standard library — no extra installs needed)
*	Run the App
Run the App
```bash
python pyproject.py
```
## 🖥️ Interface Layout

```
┌──────────────────────────────────────────────────────────┐
│  Colour Name: [___]  Brush Size: [▼]  Sheet Colour: [___] [Enter] │  ← Controls (frame1)
├──────────────────────────────────────┬───────────────────┤
│                                      │   Options         │
│         Drawing Canvas               │  [Reset] [Eraser] │
│         (1000 × 1000 px)             │                   │
│                                      │  Simple           │
│                                      │  Painting         │
│                                      │  Application      │
└──────────────────────────────────────┴───────────────────┘
``'

## 🎛️ Features & Usage
✏️ Drawing
*	Click and drag the **left mouse button** on the canvas to draw.
*	The brush renders using Unicode dot characters scaled to your chosen size.

## 🎨 Brush Colour
*	Type any valid Tkinter colour name (e.g., `red`, `blue`, `#FF5733`) into the **"Enter colour name"** field.
*	The colour updates live as you draw.

## 📏 Brush Size
*	Use the **dropdown** to select a brush size between **10** and **100** (in steps of 2).
*	Default size is **26**.

## 🖼️ Canvas (Sheet) Colour
*	Type a colour into the **"Enter sheet colour"** field and click **Enter** to apply it as the canvas background.

## 🧽 Eraser
*	Click the **Eraser** button to toggle eraser mode • this temporarily sets the brush colour to match the sheet colour.
*	Click **Eraser** again to restore your previous brush colour.

## 🔄 Reset
*	Click **Reset** to clear the canvas back to the current sheet colour.
*	Your last used brush colour is preserved after reset.

## 📁 Project Structure

```
Painting_app/
│
├── pyproject.py                  # Main application file
└── README.md                     # Project documentation
└── Painting_app_screenshot.png   # interface layout screenshot
```
## ⚠️ Known Limitations
*	Colour names must be valid Tkinter colour strings. Invalid names trigger an error dialog.
*	The eraser works by painting over in the sheet colour — it does not undo strokes.
*	Canvas content is not saveable to a file in this version.

## 🛠️ Possible Improvements
*	Save canvas as an image (PNG/JPEG)
*	Undo / Redo functionality
*	Colour picker dialog (instead of text entry)
*	Shape tools (line, rectangle, circle)
*	Stroke-based rendering for smoother lines

## 📄 License
            This project is open source. Feel free to use, modify, and distribute it.
## 🙌 Acknowledgements
             Built with Python's built-in [Tkinter](https://docs.python.org/3/library/tkinter.html) GUI toolkit.
