---
name: piuu-pip-side-edge-assist
description: Floating side-edge bar assist, vertical edge dragging, top drop removal header zone, persistent Notes repository, and quick app switcher.
---

# 🛸 Piuu PiP Side Edge Assist & Notes Skill (`piuu-pip-side-edge-assist`)

This skill documents building floating overlay services (`TYPE_APPLICATION_OVERLAY`), side-edge docking, auto-hiding, drop-to-remove drag zones, and persistent local notes storage.

---

## 📍 1. Side Edge Placement & Drag Gesture Window Management

```kotlin
val params = WindowManager.LayoutParams(
    WindowManager.LayoutParams.WRAP_CONTENT,
    WindowManager.LayoutParams.WRAP_CONTENT,
    WindowManager.LayoutParams.TYPE_APPLICATION_OVERLAY,
    WindowManager.LayoutParams.FLAG_NOT_FOCUSABLE,
    PixelFormat.TRANSLUCENT
).apply {
    gravity = Gravity.TOP or (if (config.pipEdgeSide == "left") Gravity.LEFT else Gravity.RIGHT)
    x = 0
    y = 300
}
```

---

## 🗑️ 2. Top Header Drop-to-Remove Zone (`DismissZoneComposable`)

When user drags the floating pill vertically near the top header ($Y < 150\text{px}$), display the red drop removal zone and stop the floating service on release:

```kotlin
if (isDragging && currentParams.y < 150) {
    stopSelf() // Stop floating overlay service on top drop zone release
}
```

---

## 📝 3. Persistent Local Notes Repository (`NotesRepository.kt`)

Store quick memos and launcher notes permanently using JSON payloads inside `SharedPreferences`:

```kotlin
class NotesRepository(context: Context) {
    private val prefs = context.getSharedPreferences("piuu_notes_prefs", Context.MODE_PRIVATE)
    private val _notes = MutableStateFlow<List<LauncherNote>>(emptyList())
    val notes: StateFlow<List<LauncherNote>> = _notes

    fun addNote(title: String, content: String) {
        val newNote = LauncherNote(title = title, content = content)
        val updated = listOf(newNote) + _notes.value
        _notes.value = updated
        saveToDisk(updated)
    }
}
```

---

## 🛠️ Required & Associated Agent Workspace Tools
When building overlay services, floating window controllers, or StateFlow stores, activate these tools from [`AI-Agents-Workspace-Tools-Library`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library):

- [`wc-scaffold`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-scaffold) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-scaffold.md)): Scaffolds Android Services, Compose floating views, and StateFlow repositories.
- [`wc-code-mod`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-code-mod) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-code-mod.md)): Injects window manager flag updates and coordinate calculations across Kotlin source files.
- [`wc-crash-doctor`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-crash-doctor) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-crash-doctor.md)): Isolates `BadTokenException` and overlay permission crashes from logcat.
- *Upcoming Tool Note*: `wc-pip-overlay` (Android overlay window permission checker) is scheduled for implementation.

