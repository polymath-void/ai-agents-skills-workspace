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
