---
name: agent-browser
description: Headless browser automation CLI for AI agents. Use when needing to navigate websites, fill forms, click elements, take screenshots, or interact with web pages. Supports refs-based interaction, wait states for page load detection, and multiple workflows including e-commerce, ticket booking, and data scraping.
prerequisites:
  commands: [agent-browser]
metadata:
  hermes:
    tags: [browser, automation, headless, scraping]
---

# Agent-Browser (Browser Automation CLI)

Headless browser automation for AI agents. Alternative to chrome-devtools-mcp with better page load detection.

## Core Workflow (CRITICAL Pattern)

Navigate → Wait → Snapshot → Act

1. Open page: `agent-browser open https://example.com`
2. Wait for load: `agent-browser wait --load networkidle` (ALWAYS!)
3. Get element refs: `agent-browser snapshot`
4. Interact using refs: `agent-browser click @e1`, `agent-browser fill @e2 "text"`

## Navigation & Page Load

- Open URL: `agent-browser open https://example.com`
- Wait for page load: `agent-browser wait --load`
- Wait for network idle: `agent-browser wait --load networkidle` (BEST)
- Wait for DOM ready: `agent-browser wait --domcontentloaded`
- Wait for text: `agent-browser wait --text "string"`
- Wait for JS condition: `agent-browser wait --fn "expression"`

## Snapshots & Element Interaction

Get accessibility tree with refs:

- Get snapshot: `agent-browser snapshot`
  Returns refs like: textbox "Buscar" [ref=e12], button "Buscar" [ref=e13]

Use refs for interaction:

- Click by ref: `agent-browser click @e13`
- Click by selector: `agent-browser click #submit-button`
- Click by text: `agent-browser find text "Submit" click`
- Fill input: `agent-browser fill @input1 "value1"`
- Type text: `agent-browser type @input1 "text"`
- Get element text: `agent-browser get text @e1`
- Get element HTML: `agent-browser get html @e1`

## Screenshots & Page Info

- Take screenshot: `agent-browser screenshot /path/to/image.png`
- Get page title: `agent-browser get title`
- Get page URL: `agent-browser get url`
- Get viewport size: `agent-browser get viewport`

## Mouse Control

- Move mouse: `agent-browser mouse move 100 200`
- Press button: `agent-browser mouse down left`
- Release button: `agent-browser mouse up left`
- Scroll: `agent-browser mouse wheel 100`
- Double click: `agent-browser mouse dblclick left`

## Form Filling Pattern

`agent-browser open https://example.com`
`agent-browser wait --load networkidle`
`agent-browser snapshot`
`agent-browser fill @input1 "value1"`
`agent-browser fill @input2 "value2"`
`agent-browser click @submit-button`
`agent-browser wait --load`

## Multi-Step Navigation Pattern

Step 1: `agent-browser open https://www.example.com`
`agent-browser wait --load networkidle`
Step 2: `agent-browser snapshot`, `agent-browser fill @search "product"`
`agent-browser click @search-button`
`agent-browser wait --load`
Step 3: `agent-browser snapshot`, `agent-browser click @product-link`
`agent-browser wait --load`

## Cookies & Storage

- Get cookies: `agent-browser cookies`
- Set cookie: `agent-browser cookies set session_id "abc123"`
- Clear cookies: `agent-browser cookies clear`

## Session Management

- Close browser: `agent-browser close`
- Use fresh session if daemon errors occur

## Troubleshooting

Click commands fail with "Resource temporarily unavailable":
- Use fresh session: `agent-browser close`, then `agent-browser open <url>`
- Use find instead of ref: `agent-browser find text "Submit" click`
- Add manual delay: `sleep 2` between fill and click

Page not loading (blank screenshot):
- ALWAYS use wait before interaction: `agent-browser wait --load networkidle`

Anti-bot detection:
- Use --device mobile to act like phone
- Add delays between actions
- Try mobile versions of sites (m.yoursite.org)

## Best Practices

1. ALWAYS wait after navigation (wait --load networkidle)
2. Use refs from snapshot (more reliable than selectors)
3. Close and reopen if daemon errors occur
4. Take screenshots to debug and verify actions
5. Check snapshots to ensure you're clicking right elements
6. Use mobile versions if desktop has anti-bot protection

## Common Use Cases

- E-commerce: Search → Select quantity → Add to cart
- Ticket booking: Search → Select bus → Show seats
- Data scraping: Navigate → Extract content → Save
- Form automation: Fill fields → Submit → Verify
