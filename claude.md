Architecture Notes
Frontend
Frontend: React 19 + TypeScript, Vite, MUI v9, React Router v7, Axios, oidc-client-ts
Folder structure under src/:
types/ — all shared TypeScript entity/model types. Pages, components, and services all import from here.
pages/ — each page has its own folder with index.tsx + style.ts
components/ — each component has its own folder with index.tsx + style.ts
layouts/ — layout wrappers (e.g. MainLayout)
services/ — all business logic and backend API calls (Axios clients)
context/ — React context providers (LoadingContext, NotificationContext, FormModeContext, UserInfoContext)
hooks/ — custom React hooks (e.g. useValidationErrorHandler)
styles/ — shared Emotion style snippets (shared.ts)
utils/ — pure utilities (apiError.ts, fileUtils.ts)
MUI theming is centralized in src/theme.ts.
Routing is React Router v7 driven. All routes are defined centrally in src/router.tsx using createBrowserRouter. App.tsx renders only <RouterProvider> — no routing logic elsewhere.
Styling uses Emotion CSS — use the css prop (@emotion/react) or styled() (@emotion/styled) for custom styles. Do not use plain CSS files or inline style props.
MUI icons: always use path imports (import FooIcon from '@mui/icons-material/Foo'). Named barrel imports (import { Foo } from '@mui/icons-material') may fail with Vite 8 pre-bundling. Verify the exact icon name exists in the installed package before use.
All layouts and pages must be mobile-ready using MUI Grid (responsive breakpoints). Never use fixed-width containers without breakpoint handling.
Font is Inter — bundled via @fontsource/inter (imported in main.tsx). A global MuiCssBaseline override in theme.ts applies Inter to * so all elements including third-party components (Material React Table, etc.) use it consistently. Do not rely on OS system fonts.
Page layout pattern: PageHeader (title card, rounded top corners) + pageBodyStyle box (content card, rounded bottom corners) sit flush together to form a visually connected two-part card. PageHeader has no bottom margin; pageBodyStyle has a subtle top border as a seam.
Browse-page layout pattern (e.g. ClientRecords): Single unified pageCardStyle card (border-radius: 16px, white background, shadow, overflow: hidden) containing: cardHeaderStyle row (title + Back button, padding: 20px 24px 18px), tabsWrapperStyle row (tabs + action buttons, padding: 0 24px), toolbarRowStyle (search + Search button + Clear Filters + Download, padding: 16px 24px 0), tableCardStyle (table, padding: 16px 24px 24px). Do NOT use PageHeader on browse pages. Back button: variant="outlined", borderRadius: '50px' (pill). Default tab: Approved (index 0). Search is triggered by a "Search" variant="contained" pill button, not on input change.
PageSection renders a section title + divider only when title prop is provided. Without a title, no divider is shown.
Navigation menu is hardcoded in src/services/menuService.ts. Icons are mapped in src/components/AppSidebar/index.tsx via ICON_MAP.
MainLayout has a fixed footer (copyright text). Layout constants exported from layouts/MainLayout/style.ts: HEADER_HEIGHT=64, SIDEBAR_WIDTH=250, SIDEBAR_COLLAPSED_WIDTH=64, FOOTER_HEIGHT=40.
Theme: App uses teal (#0fa79a) throughout — AppHeader logo icon, avatar background, toggle button background (#dff4f0 / hover #b2e6e0), and MenuIcon color. Never use purple (#5e35b1).
Sidebar scrollbar: Hidden via scrollbarWidth: 'none' + '&::-webkit-scrollbar': { display: 'none' } on the nav List. Do not add visible scrollbars to the sidebar nav.
ClientTable: No "Primary Contact" column in any tab variant (pending action, draft, approved, queued, rejected). Contact details are not shown in the table.