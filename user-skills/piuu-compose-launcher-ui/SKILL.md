---
name: piuu-compose-launcher-ui
description: Jetpack Compose 4-column Android standard grid, 2D matrix widget resizing, raw wallpaper background view, status bar padding fit, and responsive visual theme palettes.
---

# 📱 Piuu Compose Launcher UI Skill (`piuu-compose-launcher-ui`)

This skill documents modern Jetpack Compose UI architecture for building 60fps Android launcher interfaces, 2D grid matrix resizing, status bar margins, and raw wallpaper background rendering.

---

## 📐 1. Standard 4-Column Android Launcher Grid

Android homescreen layouts align to a 4-column grid (`GridCells.Fixed(4)`) with dynamic 1–4 column span mapping:

```kotlin
LazyVerticalGrid(
    columns = GridCells.Fixed(4),
    modifier = Modifier.fillMaxSize().padding(horizontal = 12.dp),
    horizontalArrangement = Arrangement.spacedBy(8.dp),
    verticalArrangement = Arrangement.spacedBy(10.dp)
) {
    items(
        items = page.elements,
        key = { it.element_id },
        span = { elem ->
            val requestedWidth = elem.style_props.w ?: 2
            val spanWidth = requestedWidth.coerceIn(1, 4)
            GridItemSpan(spanWidth)
        }
    ) { elem ->
        // Widget Card Rendering
    }
}
```

---

## 🖼️ 2. Raw Wallpaper Background View & Status Bar Padding Fit

To ensure the homescreen displays raw device wallpaper without forcing dark dimming masks:

```kotlin
// Default raw wallpaper background
val activeBgColor = LauncherBackground.copy(
    alpha = if (config.enableWallpaperMask) config.backgroundTransparency else 0.0f
)

Box(
    modifier = Modifier
        .fillMaxSize()
        .background(activeBgColor)
        .statusBarsPadding()
        .navigationBarsPadding()
)
```

Enforcing `.statusBarsPadding()` and `.navigationBarsPadding()` directly on the outer container Box guarantees the app drawer card and widgets respect Android system status bar and gesture navigation margins.

---

## 📐 3. Text Overflow & Ellipsis Protection

All card titles, app shortcut names, and widget headers must enforce strict single-line bounds:

```kotlin
Text(
    text = app.name,
    fontSize = 11.sp,
    fontWeight = FontWeight.Medium,
    maxLines = 1,
    overflow = TextOverflow.Ellipsis,
    textAlign = TextAlign.Center
)
```

---

## 🛠️ Required & Associated Agent Workspace Tools
When scaffolding or refactoring Jetpack Compose launcher interfaces, activate these tools from [`AI-Agents-Workspace-Tools-Library`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library):

- [`wc-scaffold`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-scaffold) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-scaffold.md)): Generates boilerplate Jetpack Compose `@Composable` component files and StateFlow repositories.
- [`wc-code-mod`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-code-mod) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-code-mod.md)): Performs safe multi-file Kotlin batch replacements (e.g. updating grid span logic).
- [`wc-analyze`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-analyze) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-analyze.md)): Profiles cyclomatic complexity and function metrics of Compose screens.
- [`wc-json-query`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/bin/wc-json-query) ([`docs`](file:///data/data/com.termux/files/home/AI-Agents-Workspace-Tools-Library/docs/tools/wc-json-query.md)): Extracts widget configuration values and dimensions from theme definitions.
- *Upcoming Tool Note*: `wc-compose-preview` (CLI Compose AST syntax validator) is tracked for subsequent implementation.

