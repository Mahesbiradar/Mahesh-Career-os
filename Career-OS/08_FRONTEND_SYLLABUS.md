# Frontend Engineering Syllabus — Mahesh Career OS

> **Goal:** Achieve practical frontend employability — sufficient for Full Stack roles and Frontend-adjacent positions.
> **Target Stack:** HTML5, CSS3, JavaScript (ES6+), React.
> **Scope:** From semantic HTML through React state management and API integration.
> **Strategy:** Focus on professional depth, not breadth. Master the core stack thoroughly.

---

## Level Structure Overview

| Level | Name | Capability Unlocked |
|-------|------|-------------------|
| Level 1 | HTML | Build well-structured, accessible pages |
| Level 2 | CSS | Style pages with layouts, responsive design |
| Level 3 | JavaScript Core | Write clean, modern JavaScript |
| Level 4 | DOM & Events | Make pages interactive |
| Level 5 | JavaScript Advanced | Async, closures, prototypes, event loop |
| Level 6 | Browser APIs | LocalStorage, fetch, history, workers |
| Level 7 | React Fundamentals | Build component-based UIs |
| Level 8 | React Hooks | Write modern functional React |
| Level 9 | React Router | Build multi-page applications |
| Level 10 | State Management | Manage complex application state |
| Level 11 | API Integration | Connect React to backend APIs |
| Level 12 | React Advanced | Performance, patterns, production |
| Level 13 | Build Tools & Ecosystem | Professional development workflow |
| Level 14 | Frontend Testing | Write and maintain UI tests |

---

## Level 1 — HTML

---

### 1.1 Document Structure & Fundamentals

- **Why It Matters:** HTML is the skeleton of every web page. Bad HTML structure breaks CSS, JavaScript, accessibility, and SEO.
- **Prerequisites:** None
- **Interview Importance:** Medium
- **Job Importance:** Critical

Topics:
- DOCTYPE declaration
- `<html>`, `<head>`, `<body>` structure
- `<meta>` tags: charset, viewport, description, author
- `<title>`
- `<link>` for stylesheets
- `<script>` placement (end of body vs `defer` vs `async`)
- HTML comments
- Character encoding (UTF-8)

---

### 1.2 Semantic HTML

- **Why It Matters:** Semantic HTML communicates meaning to browsers, screen readers, and search engines. Interviewers test this — "div vs article vs section."
- **Prerequisites:** 1.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `<div>` and `<span>` — non-semantic containers
- Semantic elements:
  - `<header>`, `<footer>`, `<main>`, `<nav>`, `<aside>`
  - `<article>`, `<section>`, `<figure>`, `<figcaption>`
  - `<time>`, `<mark>`, `<details>`, `<summary>`
  - `<address>`
- Heading hierarchy (`<h1>` through `<h6>`) — one `<h1>` per page
- `<p>`, `<ul>`, `<ol>`, `<li>`, `<dl>`, `<dt>`, `<dd>`
- `<strong>`, `<em>`, `<code>`, `<pre>`, `<blockquote>`
- When to use which element (semantic meaning vs visual appearance)

---

### 1.3 Links & Navigation

- **Why It Matters:** Navigation is core to web applications.
- **Prerequisites:** 1.2
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `<a href="...">` — anchor element
- Absolute vs relative URLs
- `target="_blank"` with `rel="noopener noreferrer"` (security)
- `href="#id"` — fragment links (same page)
- `href="mailto:"` and `href="tel:"`
- Active state for navigation links

---

### 1.4 Forms & Inputs

- **Why It Matters:** Forms are how users submit data. Every application has forms — login, registration, search, checkout.
- **Prerequisites:** 1.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `<form action method>`
- `<input>` types: text, email, password, number, tel, url, date, time, checkbox, radio, file, hidden, submit, reset, range, color
- `<textarea>`, `<select>`, `<option>`, `<optgroup>`
- `<label>` with `for` attribute (accessibility critical)
- `<fieldset>` and `<legend>`
- `<button>` types: submit, reset, button
- Input attributes: `name`, `id`, `value`, `placeholder`, `required`, `disabled`, `readonly`, `min`, `max`, `maxlength`, `pattern`, `autocomplete`
- HTML5 form validation
- `<datalist>` for suggestions
- `<output>`

---

### 1.5 Tables

- **Why It Matters:** Tables are for tabular data — reports, comparison grids, dashboards.
- **Prerequisites:** 1.2
- **Interview Importance:** Low
- **Job Importance:** Medium

Topics:
- `<table>`, `<thead>`, `<tbody>`, `<tfoot>`
- `<tr>`, `<th>`, `<td>`
- `colspan` and `rowspan`
- `<caption>`
- Accessible tables (scope attribute)
- Tables for data only (not layout)

---

### 1.6 Media Elements

- **Why It Matters:** Images, video, and audio are core to modern web applications.
- **Prerequisites:** 1.2
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `<img src alt width height loading="lazy">`
- Responsive images: `srcset`, `sizes`, `<picture>` element
- Image formats: JPEG, PNG, WebP, SVG, AVIF
- `<video>` with controls, autoplay, muted, loop
- `<audio>`
- `<iframe>` — embedding external content (YouTube, maps)
- `<svg>` inline SVG basics

---

### 1.7 Accessibility (a11y)

- **Why It Matters:** Accessibility is a legal requirement in many countries and a professional standard. Interviewers increasingly test this.
- **Prerequisites:** 1.2, 1.4
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- WCAG 2.1 guidelines (awareness)
- ARIA roles: `role="button"`, `role="navigation"`, `role="dialog"`, `role="alert"`
- `aria-label`, `aria-labelledby`, `aria-describedby`
- `aria-hidden="true"` — hide from screen readers
- `aria-expanded`, `aria-checked` — state communication
- `aria-live` regions for dynamic content
- Focus management
- Tab order and `tabindex`
- Keyboard navigation
- Skip to main content link
- Contrast ratio requirements
- Alt text for images (informative vs decorative)

---

## Level 2 — CSS

---

### 2.1 CSS Fundamentals

- **Why It Matters:** CSS controls the visual presentation of every web application. A developer who can't CSS is not hirable for frontend.
- **Prerequisites:** Level 1
- **Interview Importance:** Medium-High
- **Job Importance:** Critical

Topics:
- Stylesheets: external, internal, inline (cascade priority)
- Selectors: type, class (`.class`), ID (`#id`), attribute (`[attr]`)
- Combinators: descendant (` `), child (`>`), adjacent sibling (`+`), general sibling (`~`)
- Pseudo-classes: `:hover`, `:focus`, `:active`, `:visited`, `:first-child`, `:last-child`, `:nth-child()`, `:not()`
- Pseudo-elements: `::before`, `::after`, `::first-line`, `::first-letter`, `::placeholder`
- Units: `px`, `em`, `rem`, `%`, `vw`, `vh`, `vmin`, `vmax`, `fr` (grid)

---

### 2.2 Box Model

- **Why It Matters:** The box model is how every element is sized. Misunderstanding it causes layout bugs.
- **Prerequisites:** 2.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Content, Padding, Border, Margin
- `box-sizing: content-box` (default) vs `box-sizing: border-box` (preferred)
- Margin collapsing (vertical margins collapse; horizontal don't)
- `width`, `height`, `min-width`, `max-width`, `min-height`, `max-height`
- `overflow: visible | hidden | scroll | auto`
- `outline` vs `border` (outline doesn't affect layout)

---

### 2.3 Specificity & Cascade

- **Why It Matters:** Specificity determines which CSS rule wins. Not understanding it causes "why isn't my CSS working?" bugs.
- **Prerequisites:** 2.2
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Cascade algorithm (specificity → order → inheritance)
- Specificity calculation: inline(1000) > ID(100) > class/attr/pseudo-class(10) > type/pseudo-element(1)
- `!important` (when to use and when to avoid)
- Inheritance: which properties inherit (color, font) vs which don't (margin, padding)
- `inherit`, `initial`, `unset`, `revert` keywords
- CSS layers (`@layer` — CSS Cascade Layers)

---

### 2.4 Layout — Flexbox

- **Why It Matters:** Flexbox is the foundation of modern CSS layout. You'll use it in every UI you build.
- **Prerequisites:** 2.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**Flex Container Properties:**
- `display: flex` or `inline-flex`
- `flex-direction`: row, row-reverse, column, column-reverse
- `flex-wrap`: nowrap, wrap, wrap-reverse
- `flex-flow` (shorthand)
- `justify-content`: flex-start, flex-end, center, space-between, space-around, space-evenly
- `align-items`: flex-start, flex-end, center, baseline, stretch
- `align-content` (multi-line)
- `gap`, `row-gap`, `column-gap`

**Flex Item Properties:**
- `flex-grow`, `flex-shrink`, `flex-basis`
- `flex` shorthand (`flex: 1` = `flex: 1 1 0`)
- `align-self` (override container's align-items)
- `order`

**Patterns:**
- Centering an element (horizontally and vertically)
- Space distribution patterns
- Fixed + flexible sidebar layout
- Holy Grail layout

---

### 2.5 Layout — CSS Grid

- **Why It Matters:** CSS Grid is the most powerful layout system ever added to CSS. Required for complex layouts.
- **Prerequisites:** 2.4
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:

**Grid Container Properties:**
- `display: grid`
- `grid-template-columns`, `grid-template-rows`
- `fr` unit (fractional)
- `repeat()` function
- `minmax()` function
- `auto-fill` vs `auto-fit`
- `grid-template-areas`
- `gap`
- `justify-items`, `align-items`, `place-items`
- `justify-content`, `align-content`

**Grid Item Properties:**
- `grid-column-start`, `grid-column-end`, `grid-row-start`, `grid-row-end`
- `grid-column`, `grid-row` shorthands
- `grid-area` (name or row/column span)
- `span` keyword
- `justify-self`, `align-self`, `place-self`

**Patterns:**
- 12-column grid system
- Dashboard layout
- Card grid with auto-fill
- Overlapping elements

---

### 2.6 Positioning

- **Why It Matters:** Understanding position is essential for dropdowns, modals, tooltips, and sticky headers.
- **Prerequisites:** 2.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `position: static` (default, in normal flow)
- `position: relative` (offset from normal position, creates stacking context)
- `position: absolute` (removed from flow, positioned relative to nearest positioned ancestor)
- `position: fixed` (relative to viewport)
- `position: sticky` (hybrid: relative until threshold, then fixed)
- `top`, `right`, `bottom`, `left` properties
- `z-index` and stacking context
- Containing block concept

---

### 2.7 Responsive Design

- **Why It Matters:** Every UI must work on mobile. Responsive design is non-negotiable.
- **Prerequisites:** 2.4, 2.5
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `<meta name="viewport" content="width=device-width, initial-scale=1">`
- Media queries: `@media (max-width: 768px) { ... }`
- Breakpoints: common patterns (320px, 576px, 768px, 992px, 1200px)
- Mobile-first vs Desktop-first approach (mobile-first preferred)
- Fluid typography: `clamp(min, preferred, max)`
- Responsive images (`max-width: 100%`)
- Container queries (`@container`)
- CSS variables for theme values

---

### 2.8 CSS Custom Properties (Variables)

- **Why It Matters:** CSS variables enable theming, reduce repetition, and enable JavaScript integration.
- **Prerequisites:** 2.1
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Declaring: `--color-primary: #3498db;`
- Using: `color: var(--color-primary);`
- Fallback: `var(--color-missing, #333)`
- Scope: `:root` for global, element for local
- JavaScript access: `getComputedStyle(el).getPropertyValue('--color')`
- Dark mode with CSS variables
- Component-level theming

---

### 2.9 Animations & Transitions

- **Why It Matters:** Smooth interactions are expected in modern UIs.
- **Prerequisites:** 2.6
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `transition`: property duration timing-function delay
  - Transition properties: opacity, transform, color, background
  - Timing functions: ease, linear, ease-in, ease-out, cubic-bezier
- `@keyframes` definition
- `animation`: name duration timing-function delay iteration-count direction fill-mode
- `animation-play-state`
- `transform`: translate, rotate, scale, skew, perspective, matrix
- GPU-accelerated properties: opacity, transform (prefer these)
- `will-change` (hint for browser optimization)
- `prefers-reduced-motion` media query

---

## Level 3 — JavaScript Core

---

### 3.1 Variables & Data Types

- **Why It Matters:** JavaScript's type system has many quirks that cause bugs. Understanding it prevents them.
- **Prerequisites:** None (but HTML/CSS helps)
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `var`, `let`, `const` (differences and when to use)
- Hoisting: `var` hoisted and initialized to `undefined`; `let`/`const` hoisted but TDZ
- Primitive types: `number`, `string`, `boolean`, `null`, `undefined`, `symbol`, `bigint`
- Reference type: `object` (includes arrays, functions)
- `typeof` operator (quirks: `typeof null === 'object'`)
- Strict equality (`===`) vs loose equality (`==`) and type coercion
- Truthy and falsy values
- `NaN`: not equal to itself (`NaN !== NaN`); use `Number.isNaN()`

---

### 3.2 Functions

- **Why It Matters:** Functions are first-class citizens in JavaScript. Every JS pattern revolves around them.
- **Prerequisites:** 3.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Function declaration (`function name() {}`) — hoisted
- Function expression (`const f = function() {}`) — not hoisted
- Arrow functions (`const f = () => {}`)
  - No own `this`
  - No `arguments` object
  - Cannot be used as constructors
  - Implicit return for single expressions
- Default parameters
- Rest parameters (`...args`)
- Spread operator (`...array`)
- `arguments` object (avoid in modern code; use rest params)
- Function as first-class value (pass to functions, return from functions)
- Immediately Invoked Function Expression (IIFE)

---

### 3.3 Scope & Closures

- **Why It Matters:** Closures power callbacks, the module pattern, and most JavaScript frameworks.
- **Prerequisites:** 3.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Lexical scope (scope determined by position in source code)
- Block scope (`let`, `const`) vs Function scope (`var`)
- Global scope
- Scope chain
- Closure: function retains reference to its outer scope even after outer function returns
- Common closure patterns: factory functions, memoization, module pattern
- Classic closure bug with `var` in loops (fixed with `let`)
- Memory implications of closures

---

### 3.4 `this` Keyword

- **Why It Matters:** `this` is JavaScript's most confusing feature. Interviewers test it constantly.
- **Prerequisites:** 3.3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `this` is determined at call time, not definition time (except arrow functions)
- Default binding: `this` is `window`/`undefined` (strict mode) in standalone call
- Implicit binding: `obj.method()` → `this` is `obj`
- Explicit binding: `call()`, `apply()`, `bind()`
- `new` binding: `this` is the new object
- Arrow functions: `this` inherited from enclosing lexical scope
- `this` in class methods
- `this` in event handlers

---

### 3.5 Prototypes & Inheritance

- **Why It Matters:** JavaScript's inheritance model is prototype-based. Understanding it explains how classes work under the hood.
- **Prerequisites:** 3.4
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Every object has a prototype (`[[Prototype]]`)
- `Object.getPrototypeOf(obj)`, `obj.__proto__` (avoid)
- Prototype chain lookup
- `Object.prototype` at the top of chain
- Prototypal inheritance
- ES6 Classes (syntactic sugar over prototypes)
  - `class` declaration
  - `constructor`
  - `extends` and `super`
  - `instanceof`
- `Object.create(proto)` — create object with specific prototype
- `hasOwnProperty()`

---

### 3.6 ES6+ Features

- **Why It Matters:** Modern JavaScript requires ES6+. If you don't know ES6+, your code looks outdated and you can't read modern codebases.
- **Prerequisites:** 3.4
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Destructuring:
  - Array: `const [a, b] = [1, 2]`
  - Object: `const { name, age } = person`
  - With renaming: `const { name: personName } = person`
  - With defaults: `const { role = 'user' } = user`
  - Nested destructuring
- Template literals: `` `Hello ${name}` ``
- Spread operator: `[...arr]`, `{...obj}`
- Rest parameters: `function f(...args) {}`
- Optional chaining: `user?.address?.city`
- Nullish coalescing: `value ?? 'default'` (only null/undefined, not 0 or '')
- Logical assignment: `||=`, `&&=`, `??=`
- Short-circuit evaluation
- `for...of` loop (iterables)
- `for...in` loop (object keys — use with caution)
- Computed property names: `{ [key]: value }`
- Method shorthand: `{ greet() {} }` instead of `{ greet: function() {} }`
- `Object.keys()`, `Object.values()`, `Object.entries()`, `Object.fromEntries()`
- `Object.assign()` and spread for object copying

---

### 3.7 Array Methods

- **Why It Matters:** Functional array operations are the most common operations in any JS codebase.
- **Prerequisites:** 3.6
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:

**Non-mutating (return new array/value):**
- `map(fn)` — transform each element
- `filter(fn)` — keep elements matching condition
- `reduce(fn, initial)` — accumulate to single value
- `find(fn)` — first matching element (or undefined)
- `findIndex(fn)` — index of first match (or -1)
- `some(fn)` — true if any element matches
- `every(fn)` — true if all elements match
- `flat(depth)` — flatten nested arrays
- `flatMap(fn)` — map + flat
- `slice(start, end)` — extract portion
- `concat(...arrays)` — combine arrays

**Mutating (modify in place):**
- `push()`, `pop()` — end of array
- `unshift()`, `shift()` — start of array
- `splice(start, deleteCount, ...items)` — add/remove at position
- `sort(compareFn)` — sort in place (default is string sort!)
- `reverse()`
- `fill(value, start, end)`

**Other:**
- `indexOf()`, `lastIndexOf()`
- `includes()`
- `join(separator)`
- `Array.from()` — create array from array-like/iterable
- `Array.isArray()`
- `Array.of()`

---

### 3.8 Modules

- **Why It Matters:** Every React project uses ES modules. Modern JavaScript is modular JavaScript.
- **Prerequisites:** 3.6
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `export` (named) and `export default`
- `import { name } from './module'`
- `import defaultExport from './module'`
- `import * as module from './module'`
- Re-exports: `export { name } from './module'`
- Dynamic imports: `import('./module').then(m => ...)`
- Module scope (no global scope leakage)
- `type="module"` in script tag
- CommonJS (`require`/`module.exports`) — Node.js legacy
- ES Modules vs CommonJS differences
- `package.json` type field (`"type": "module"`)

---

## Level 4 — DOM Manipulation

---

### 4.1 DOM Tree & Navigation

- **Why It Matters:** The DOM is the programmatic interface to HTML. JavaScript manipulates the DOM to make pages dynamic.
- **Prerequisites:** Level 3
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- DOM tree: document → html → head/body → elements
- `document` object
- Node types: Element, Text, Comment, Document
- Selecting elements:
  - `getElementById()`
  - `getElementsByClassName()` (live HTMLCollection)
  - `getElementsByTagName()` (live HTMLCollection)
  - `querySelector()` (first match)
  - `querySelectorAll()` (NodeList — static)
- DOM navigation:
  - `parentElement`, `children`, `firstElementChild`, `lastElementChild`
  - `nextElementSibling`, `previousElementSibling`
- `closest()` — find ancestor matching selector

---

### 4.2 DOM Manipulation

- **Why It Matters:** Creating, updating, and removing elements is how JavaScript UIs work.
- **Prerequisites:** 4.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `innerHTML`, `textContent` (vs `innerText`)
- `createElement()`, `createTextNode()`
- `appendChild()`, `prepend()`, `append()`
- `insertBefore()`, `insertAdjacentElement()`
- `removeChild()`, `remove()`
- `cloneNode(deep)`
- `setAttribute()`, `getAttribute()`, `removeAttribute()`
- `element.style.property = value`
- `classList`: `.add()`, `.remove()`, `.toggle()`, `.contains()`
- `dataset` (data-* attributes)
- Creating a complex DOM structure efficiently (DocumentFragment)

---

### 4.3 Event Handling

- **Why It Matters:** Events make pages interactive. Every UI interaction — click, input, scroll — is an event.
- **Prerequisites:** 4.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `addEventListener(type, handler, options)`
- `removeEventListener()`
- Event types: click, dblclick, mouseenter, mouseleave, mouseover, mouseout, mousemove, keydown, keyup, keypress, input, change, submit, focus, blur, scroll, resize, load, DOMContentLoaded
- Event object properties: `target`, `currentTarget`, `type`, `key`, `keyCode`, `clientX/Y`, `pageX/Y`
- `event.preventDefault()` — stop default behavior
- `event.stopPropagation()` — stop bubbling

---

### 4.4 Event Bubbling & Delegation

- **Why It Matters:** Event delegation is a critical performance pattern. Interviewers test it.
- **Prerequisites:** 4.3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Event propagation phases: Capture → Target → Bubble
- Bubbling: event propagates up the DOM tree
- Capturing: event propagates down (use `{capture: true}`)
- `stopPropagation()` vs `stopImmediatePropagation()`
- Event delegation:
  - Attach one listener to parent, handle events from children
  - Uses `event.target` to identify the child
  - Benefits: fewer event listeners, works for dynamically added elements
  - Pattern: check `event.target.matches(selector)`
- Custom events: `new CustomEvent('name', { detail: data, bubbles: true })`

---

## Level 5 — JavaScript Advanced

---

### 5.1 Promises

- **Why It Matters:** Promises replaced callback hell. All modern async JavaScript uses promises.
- **Prerequisites:** Level 3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Promise states: Pending, Fulfilled, Rejected
- `new Promise((resolve, reject) => {})`
- `.then()`, `.catch()`, `.finally()`
- Promise chaining
- `Promise.resolve()`, `Promise.reject()`
- `Promise.all()` — all must succeed
- `Promise.allSettled()` — all must complete (success or failure)
- `Promise.race()` — first to settle wins
- `Promise.any()` — first to fulfill wins
- Error handling in promise chains
- Unhandled promise rejections

---

### 5.2 Async/Await

- **Why It Matters:** `async/await` is the modern way to write asynchronous code. Cleaner than promise chains.
- **Prerequisites:** 5.1
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `async function` returns a Promise
- `await` pauses execution within async function
- Error handling: `try/catch/finally` with async/await
- Sequential vs parallel execution:
  - Sequential: `const a = await fetchA(); const b = await fetchB()`
  - Parallel: `const [a, b] = await Promise.all([fetchA(), fetchB()])`
- `await` in loops (for...of vs forEach difference)
- Top-level await (in modules)
- Async iteration (`for await...of`)
- Converting promise chains to async/await

---

### 5.3 The Event Loop

- **Why It Matters:** The event loop explains why async JavaScript works, why setTimeout is not precise, and why Promises execute before timeouts.
- **Prerequisites:** 5.2
- **Interview Importance:** Critical
- **Job Importance:** High

Topics:
- JavaScript is single-threaded
- Call stack: LIFO, executes synchronous code
- Web APIs (browser): setTimeout, fetch, DOM events — run outside call stack
- Callback queue (Macrotask queue): setTimeout, setInterval, I/O, UI rendering
- Microtask queue: Promises (`.then`), `queueMicrotask`, `MutationObserver`
- Event loop algorithm:
  1. Execute all synchronous code
  2. Execute all microtasks (drain queue)
  3. Execute one macrotask
  4. Execute all microtasks again
  5. Repeat
- Why Promises (.then) execute before setTimeout even with 0ms timeout
- `queueMicrotask()` API
- `requestAnimationFrame()` — pre-paint callback

---

### 5.4 Debounce & Throttle

- **Why It Matters:** Performance optimization for search inputs, scroll handlers, resize handlers.
- **Prerequisites:** 5.3
- **Interview Importance:** High — frequently implemented in interviews
- **Job Importance:** Critical

Topics:
- **Debounce:** delay function execution; reset timer on each call (execute after user stops)
  - Use case: search-as-you-type (don't call API on every keystroke)
  - Implementation from scratch
- **Throttle:** execute at most once per time period
  - Use case: scroll handler, resize handler
  - Implementation from scratch
- Leading vs trailing edge debounce
- `lodash.debounce`, `lodash.throttle`

---

### 5.5 JavaScript Design Patterns

- **Why It Matters:** Common patterns appear in frameworks and professional code.
- **Prerequisites:** Level 3-5
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- **Module Pattern:** encapsulation via closures (IIFE)
- **Observer / Pub-Sub Pattern:** subscribe to events
- **Singleton Pattern:** only one instance
- **Factory Pattern:** create objects without specifying class
- **Strategy Pattern:** interchange algorithms
- **Proxy Pattern:** intercept operations (JavaScript `Proxy` object)
- **Mediator Pattern:** centralized communication
- SOLID principles applied to JavaScript

---

## Level 6 — Browser APIs

---

### 6.1 Web Storage

- **Why It Matters:** Frontend state persistence uses localStorage. Authentication tokens, preferences.
- **Prerequisites:** Level 3
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- **localStorage:** persistent; survives browser restart; string only; 5-10MB limit
- **sessionStorage:** per-tab; cleared on tab close
- Methods: `setItem(key, value)`, `getItem(key)`, `removeItem(key)`, `clear()`
- Storing objects: `JSON.stringify()` on write, `JSON.parse()` on read
- `storage` event (cross-tab communication)
- localStorage vs sessionStorage vs cookies vs IndexedDB
- Security: localStorage is accessible to JavaScript (XSS vulnerability)
- `IndexedDB`: large, structured data storage (awareness)

---

### 6.2 Fetch API

- **Why It Matters:** The Fetch API replaces XMLHttpRequest for making HTTP requests.
- **Prerequisites:** 5.1, 5.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- `fetch(url, options)` returns a Promise
- Options: `method`, `headers`, `body`, `credentials`, `mode`, `signal`
- Response methods: `.json()`, `.text()`, `.blob()`, `.arrayBuffer()`
- Response properties: `ok`, `status`, `statusText`, `headers`
- Two-step process: fetch returns response, then call .json()
- Error handling: fetch only rejects on network failure, not HTTP errors!
- `AbortController` for cancelling requests
- CORS implications
- Fetch vs Axios comparison

---

### 6.3 History API

- **Why It Matters:** SPAs manipulate browser history without page reloads. React Router uses this.
- **Prerequisites:** Level 3
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- `history.pushState(state, title, url)` — add history entry
- `history.replaceState(state, title, url)` — replace current entry
- `history.back()`, `forward()`, `go(n)`
- `window.location` — current URL info
- `popstate` event — triggered by back/forward navigation
- Hash-based routing vs History API routing (tradeoffs)

---

## Level 7 — React Fundamentals

---

### 7.1 React Introduction

- **Why It Matters:** React is the most widely used frontend framework. Understanding its core model is fundamental.
- **Prerequisites:** Level 3-6
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- What problem React solves (imperative DOM manipulation → declarative components)
- Virtual DOM concept and reconciliation
- Component-based architecture
- Unidirectional data flow
- React's rendering model
- Setting up React: Create React App, Vite (preferred), Next.js
- Project structure conventions

---

### 7.2 JSX

- **Why It Matters:** JSX is how React components are written. It's not HTML — knowing the differences prevents bugs.
- **Prerequisites:** 7.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- JSX is syntactic sugar for `React.createElement()`
- JSX vs HTML differences:
  - `className` not `class`
  - `htmlFor` not `for`
  - `camelCase` event handlers (`onClick`, `onChange`)
  - Self-closing tags required (`<br />`)
  - Expressions in `{}`
- JSX children
- Fragments: `<>...</>` or `<React.Fragment>`
- JSX conditional rendering:
  - Ternary: `{condition ? <A /> : <B />}`
  - Short-circuit: `{condition && <A />}`
  - Null for nothing: `{condition ? <A /> : null}`
- JSX lists (always need key)

---

### 7.3 Components

- **Why It Matters:** Components are React's fundamental building block.
- **Prerequisites:** 7.2
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Functional components (modern standard)
- Class components (legacy — must recognize in code reviews)
- Component naming (PascalCase)
- Pure components (same props → same output)
- Composing components
- Container vs Presentational component pattern
- Component hierarchy design

---

### 7.4 Props

- **Why It Matters:** Props are how parent components pass data to children. The backbone of component communication.
- **Prerequisites:** 7.3
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Props are read-only (one-way data flow)
- Passing strings, numbers, booleans, objects, arrays, functions as props
- Default props
- `children` prop
- Prop destructuring
- Spread props (`<Component {...props} />`)
- PropTypes (runtime validation — `prop-types` library)
- TypeScript for compile-time prop validation

---

### 7.5 State (useState)

- **Why It Matters:** State is what makes React components dynamic. Every interactive component has state.
- **Prerequisites:** 7.4
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- `const [state, setState] = useState(initialValue)`
- State is private to the component
- `setState()` triggers re-render
- State updates are asynchronous (batched in React 18)
- Functional updates: `setState(prev => prev + 1)`
- State initialization: function form for expensive initial computation
- Multiple state variables vs object state
- State immutability — never mutate state directly
- Lifting state up (share between siblings via common ancestor)

---

### 7.6 Lists & Keys

- **Why It Matters:** Rendering lists is fundamental. The key requirement is both important and frequently misunderstood.
- **Prerequisites:** 7.5
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Rendering arrays with `.map()`
- `key` prop: unique identifier per list item
- Why keys matter (reconciliation efficiency)
- Keys must be stable, unique among siblings
- `index` as key — when it's okay (static lists) vs when it breaks (reorderable lists)
- Keys don't pass to component as props (must use different prop name)

---

## Level 8 — React Hooks

---

### 8.1 useEffect

- **Why It Matters:** `useEffect` manages side effects (API calls, subscriptions, timers). Misunderstanding it causes infinite loops and memory leaks.
- **Prerequisites:** Level 7
- **Interview Importance:** Critical
- **Job Importance:** Critical

Topics:
- Side effects: API calls, DOM manipulation, subscriptions, timers
- `useEffect(fn, dependencies)`
- Dependency array:
  - No array: runs after every render
  - Empty array `[]`: runs once on mount (componentDidMount equivalent)
  - With deps: runs when dependencies change
- Cleanup function (return from effect):
  - Removes subscriptions, clears timers
  - Runs before re-running effect and on unmount
- Common patterns: fetching data on mount, event listener setup, interval
- Infinite loop prevention (missing/wrong dependencies)
- `useEffect` vs `useLayoutEffect`
- React 18 Strict Mode double-invocation

---

### 8.2 useRef

- **Why It Matters:** useRef is needed for DOM access, storing mutable values without re-renders, and preserving values across renders.
- **Prerequisites:** 8.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `const ref = useRef(initialValue)`
- `ref.current` — mutable, doesn't trigger re-render
- DOM ref: `<div ref={ref}>` → `ref.current` is the DOM element
- Storing previous values
- Storing interval/timeout IDs
- `useRef` vs `useState` (when to use which)
- `forwardRef` — forward ref to child component
- `useImperativeHandle` — customize exposed ref interface

---

### 8.3 useContext

- **Why It Matters:** Context solves "prop drilling" — passing props through many intermediate components.
- **Prerequisites:** 8.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `React.createContext(defaultValue)`
- `Context.Provider` — provide value
- `useContext(Context)` — consume value
- Context re-render behavior (all consumers re-render on context change)
- Multiple contexts
- Context performance optimization (split contexts, memoize values)
- Context vs prop drilling vs state management library (when to use each)

---

### 8.4 useReducer

- **Why It Matters:** useReducer is preferred for complex state logic — multiple sub-values or next state depends on previous state.
- **Prerequisites:** 8.3
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- `const [state, dispatch] = useReducer(reducer, initialState)`
- Reducer function: `(state, action) => newState`
- Action object: `{ type: 'ACTION_TYPE', payload: data }`
- Dispatching actions
- State immutability in reducer
- `useReducer` vs `useState` (when to choose)
- Context + useReducer pattern (Redux-lite)
- Lazy initialization: `useReducer(reducer, initialArg, init)`

---

### 8.5 useCallback & useMemo

- **Why It Matters:** These are React's memoization hooks. Used to prevent unnecessary re-renders and expensive recalculations.
- **Prerequisites:** 8.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- **useMemo:** memoize expensive calculated values
  - `const value = useMemo(() => compute(a, b), [a, b])`
  - Only recalculates when dependencies change
- **useCallback:** memoize function references
  - `const fn = useCallback(() => { ... }, [deps])`
  - Prevents child re-renders when passing callbacks as props
- When to memoize (profiling first!)
- Over-memoization problems
- `React.memo` — memoize component
- `React.memo` + `useCallback` pattern for optimized child components

---

### 8.6 Custom Hooks

- **Why It Matters:** Custom hooks are how you extract and reuse stateful logic between components.
- **Prerequisites:** Level 8
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Naming convention: `use` prefix required
- Extracting stateful logic from components
- Custom hooks can use other hooks
- Common custom hooks to build:
  - `useFetch` — data fetching with loading/error state
  - `useLocalStorage` — sync state with localStorage
  - `useDebounce` — debounce a value
  - `useWindowSize` — responsive breakpoints
  - `usePrevious` — track previous value
  - `useOnClickOutside` — detect clicks outside element
- Sharing logic without sharing state
- Third-party hook libraries (react-use, ahooks)

---

## Level 9 — React Router

---

### 9.1 React Router Fundamentals

- **Why It Matters:** Every multi-page React application uses React Router.
- **Prerequisites:** Level 7-8
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Client-side routing vs server-side routing
- `BrowserRouter` vs `HashRouter` vs `MemoryRouter`
- `Routes` and `Route` components
- `Link` and `NavLink` components
- Route path matching
- `index` routes

---

### 9.2 Dynamic Routes & Navigation

- **Why It Matters:** Real applications have dynamic URLs — `/users/:id`, `/products/:category/:id`.
- **Prerequisites:** 9.1
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- URL parameters: `/users/:id` → `useParams()`
- Query string: `useSearchParams()`
- Programmatic navigation: `useNavigate()`
- `navigate('/path', { replace: true, state: data })`
- `useLocation()` — current location object
- `<Outlet />` — nested routes
- Nested routing patterns

---

### 9.3 Protected Routes

- **Why It Matters:** Authentication-gated routes are in every real application.
- **Prerequisites:** 9.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Pattern: check auth state, redirect to login if not authenticated
- `<Navigate>` component for declarative redirects
- Storing return URL for post-login redirect
- Role-based route protection
- Lazy loading routes (`React.lazy` + `Suspense`)

---

## Level 10 — State Management

---

### 10.1 State Management Landscape

- **Why It Matters:** Large applications need global state. Choosing the right tool is a system design question.
- **Prerequisites:** Level 8-9
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Local state (useState, useReducer) — component-specific
- Shared state (Context + useReducer) — small/medium apps
- External state managers — large/complex apps
- Server state (data from API) vs client state (UI state)

---

### 10.2 Redux Toolkit

- **Why It Matters:** Redux Toolkit is the standard for large-scale React applications. Many job descriptions list it.
- **Prerequisites:** 10.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Redux core concepts: store, actions, reducers
- Redux Toolkit `createSlice()`:
  - `initialState`
  - `reducers` (with Immer for mutable-style updates)
  - Action creators auto-generated
- `configureStore()`
- `useSelector()` — read state
- `useDispatch()` — dispatch actions
- `createAsyncThunk()` — async actions (API calls)
- RTK Query (data fetching layer)
- Redux DevTools

---

### 10.3 Zustand

- **Why It Matters:** Zustand is the modern lightweight alternative. Simple, unopinionated, growing rapidly.
- **Prerequisites:** 10.1
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- `create()` — create a store
- `set()` for updates (Immer-style)
- `get()` for reading state
- Selecting with `useStore(store, selector)`
- Computed values
- Async actions
- Middleware (persist, devtools)
- Zustand vs Redux comparison

---

## Level 11 — API Integration

---

### 11.1 Data Fetching Patterns

- **Why It Matters:** Every real application fetches data from an API. This is the core integration skill.
- **Prerequisites:** Level 8, 5.2
- **Interview Importance:** High
- **Job Importance:** Critical

Topics:
- Basic pattern: `useEffect` + `useState` (loading, data, error)
- Race conditions in useEffect (stale closures, cleanup)
- `AbortController` for cancelling fetches
- Avoiding waterfall requests (parallel fetching)
- Optimistic updates

---

### 11.2 React Query (TanStack Query)

- **Why It Matters:** React Query is the industry standard for server state management. Eliminates 80% of custom data fetching code.
- **Prerequisites:** 11.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Why React Query (caching, deduplication, background refresh, retry)
- `useQuery(key, fetcher)` — fetch and cache data
- Query keys: unique identifier for cached data
- Loading, error, data states
- `staleTime` and `cacheTime`
- `useMutation()` — create/update/delete operations
- `invalidateQueries()` — refetch after mutation
- Optimistic updates with `useMutation`
- `useInfiniteQuery` — infinite scroll
- `QueryClient` and `QueryClientProvider`

---

## Level 12 — React Advanced

---

### 12.1 Code Splitting & Lazy Loading

- **Why It Matters:** Large bundles slow initial load. Code splitting loads code only when needed.
- **Prerequisites:** Level 7-11
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- `React.lazy()` and `import()` dynamic imports
- `Suspense` fallback
- Route-based code splitting
- Component-based code splitting
- Named exports with lazy (wrapper needed)
- `@loadable/component` alternative

---

### 12.2 Error Boundaries

- **Why It Matters:** JavaScript errors in components shouldn't crash the entire UI. Error boundaries catch them.
- **Prerequisites:** Level 7
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Error boundaries catch rendering errors in child components
- Only class components can be error boundaries (as of React 18)
- `componentDidCatch()` and `static getDerivedStateFromError()`
- Where to place error boundaries
- `react-error-boundary` library

---

### 12.3 Performance Optimization

- **Why It Matters:** React performance issues are real at scale. Knowing how to profile and fix them is expected at senior level.
- **Prerequisites:** 8.5
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- React DevTools Profiler
- When to optimize (measure first!)
- Preventing unnecessary re-renders:
  - `React.memo`
  - `useCallback` for stable function references
  - `useMemo` for expensive calculations
- State colocation (keep state as low as possible)
- Context splitting (avoid large context re-renders)
- Virtual lists for long lists (`react-virtual`, `react-window`)
- Production build optimization

---

## Level 13 — Build Tools & Ecosystem

---

### 13.1 Package Management

- **Why It Matters:** Every project uses a package manager.
- **Prerequisites:** Level 7
- **Interview Importance:** Low
- **Job Importance:** Critical

Topics:
- npm: `install`, `install --save-dev`, `scripts`, `package.json`, `package-lock.json`
- yarn: `add`, `add --dev`
- pnpm: disk-space efficient
- Semantic versioning: `^` (compatible), `~` (patch only), exact
- `node_modules` and why it's gitignored
- Peer dependencies
- `npm audit` for security

---

### 13.2 Vite

- **Why It Matters:** Vite has replaced Create React App as the standard React build tool.
- **Prerequisites:** 13.1
- **Interview Importance:** Medium
- **Job Importance:** High

Topics:
- Why Vite (fast dev server via native ESM, fast HMR)
- Vite vs CRA vs Webpack
- `vite.config.js`
- Environment variables (`import.meta.env.VITE_*`)
- Build output
- Plugins ecosystem

---

### 13.3 TypeScript with React

- **Why It Matters:** TypeScript is now the standard in professional React development. Job descriptions increasingly require it.
- **Prerequisites:** Level 7, JavaScript types knowledge
- **Interview Importance:** High
- **Job Importance:** High (growing)

Topics:
- Why TypeScript (catch errors at compile time)
- TypeScript + React setup (TSX files)
- Typing props: `interface Props { ... }` or `type Props = { ... }`
- Typing `useState`: `useState<User | null>(null)`
- Typing event handlers: `React.ChangeEvent<HTMLInputElement>`
- Typing refs: `useRef<HTMLDivElement>(null)`
- Typing context
- Generic components
- `React.FC` type (and why some avoid it)

---

## Level 14 — Frontend Testing

---

### 14.1 Testing Fundamentals

- **Why It Matters:** Frontend code must be tested. Interviewers ask about testing strategy.
- **Prerequisites:** Level 7-11
- **Interview Importance:** Medium-High
- **Job Importance:** High

Topics:
- Testing pyramid: Unit → Integration → E2E
- What to test in React (behavior, not implementation)
- "Test as the user would" principle
- Coverage metrics

---

### 14.2 Jest & React Testing Library

- **Why It Matters:** Jest + RTL is the standard for React unit/integration testing.
- **Prerequisites:** 14.1
- **Interview Importance:** High
- **Job Importance:** High

Topics:
- Jest: test runner + assertion library
- `describe()`, `it()`/`test()`, `expect()`
- `beforeEach()`, `afterEach()`, `beforeAll()`, `afterAll()`
- Jest matchers: `toBe`, `toEqual`, `toBeInTheDocument`, `toHaveTextContent`
- React Testing Library:
  - `render()` component
  - Queries: `getByRole`, `getByText`, `getByLabelText`, `getByPlaceholderText`
  - `screen` object
  - `userEvent` for realistic interactions
  - `waitFor()` for async assertions
  - `findBy*` for async elements
- Mocking: `jest.fn()`, `jest.mock()`
- Testing async components
- Testing forms
- Testing API calls (mock fetch)

---

### 14.3 E2E Testing with Cypress (Awareness)

- **Why It Matters:** Cypress is the standard E2E testing tool. Awareness expected.
- **Prerequisites:** 14.2
- **Interview Importance:** Low-Medium
- **Job Importance:** Medium

Topics:
- What E2E tests cover (full user flows)
- Cypress test structure
- `cy.visit()`, `cy.get()`, `cy.click()`, `cy.type()`
- Cypress vs Playwright
- When to use E2E (critical user paths)

---

*This is the knowledge inventory for Frontend Engineering. Roadmap and scheduling are managed separately.*
