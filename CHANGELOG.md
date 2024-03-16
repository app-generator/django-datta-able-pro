# Change Log

## [1.0.26] 2024-03-16
### Changes

- Fixes:
  - DT Page (dark mode)
  - Profile Page (dark mode)
  - Added Redis to Docker 
  - Profile Page - Fix JS Browser Error 
  - #79 - Invalid block tag on `index-1.html`

## [1.0.25] 2024-03-11
### Changes

- Fixes:
  - dataTables layout
- Added Automatized Tests
  - Linux
  - Windows
- Added [Delivery Tests](./test_reports/2024-03-11)
  - [HTML](./test_reports/2024-03-11/report.html)
  - [Video](./test_reports/2024-03-11/spec.cy.js.mp4)

## [1.0.24] 2024-02-29
### Changes

- Update DEMO Link
  - [Datta Able PRO Django](https://django-datta-pro.onrender.com/)

## [1.0.23] 2024-02-27
### Changes

- Update DOCS (readme)
  - Added `Celery` Section 

## [1.0.22] 2024-02-10
### Changes

- Update DEMO Url
- Updare README (minor)

## [1.0.21] 2024-02-10
### Changes

- Added Error Pages
  - 400, 403, 500

## [1.0.20] 2024-02-08
### Changes

- Added DB Switch in Configuration

## [1.0.19] 2024-02-08
### Changes

- Update profile
  - Added BIO (managed by Quill)

## [1.0.18] 2024-02-07
### Changes

- Update README (docs)
- Update Docker
- New Apps:
  - charts
  - api
  - celery
  - file manager
  - dark mode 
  - i18n (internationalization) 

## [1.0.17] 2024-01-27
### Changes

- Profile Page Improvements

## [1.0.16] 2023-12-06
### Fixes

- #32: My Profile --> Edit screen is not showing existing values.
- #29: Superuser - Users List not visible
- #26: collectstatic bumps errors

## [1.0.15] 2023-12-05
### Fixes

- #28: Profile Image - SuperUser & Common User are broken
- #29: Superuser - Users List not visible

## [1.0.14] 2023-08-13
### Changes

- Fix #7, collectstatic bumps errors
- Remove `ASSETS_ROOT` variable
- Added `Render` Support (CI/CD)

## [1.0.13] 2023-08-01
### Changes

- Remove Broken Link
  - `index-chart-package.html`
  
## [1.0.12] 2022-08-21
### Fixes & Improvements

- Fix `Docker` Set Up
- Fix broken link (sidebar)

## [1.0.11] 2022-08-08
### Improvements

- **Social Login** via `Github` & `Twitter`
- `Change password`, `Self Deletion`
- `Authentication` via email OR username

## [1.0.10] 2022-07-21
### Fixes

- Fix broken links on `LIVE Configurator`
- `elements-ac_tour.html` - fix broken template

## [1.0.9] 2022-07-10
### Fixes

- FTP Upload
  - Better error checking
- Users management
  - Fixes   

## [1.0.8] 2022-07-10
### Improvements

- Improved Authentication
  - Visual password strength indicator (registration)
  - Suspend user after 3 failed login attempts
- New Feature: `User Profiles`
  - Extended User profile
  - Added Superusers
  - Image upload via `FTP`

## [1.0.7] 2022-06-13
### Improvements

- Built with [Datta Able PRO Generator](https://appseed.us/generator/datta-able-pro/)
  - Timestamp: `2022-06-13 11:37`
- Improved `Auth UX`
- `Dynamic API` - temporary removal
  - This feature is scheduled for generator integration

## [1.0.6] 2022-05-31
### Improvements

- Added Dynamic API  
  - All registered models enabled in `CFG` expose DRF CRUD via `/api/<MODEL_NAME>/` URI

## [1.0.5] 2022-05-30
### Fixes & Improvements

- Bump UI to `Datta Able PRO v1.0.0`
- Improved `Docker`
- Improved Codebase
- Fix broken links 
- Fix Assets path (Chart.js was Uppercased)

## [1.0.4] 2021-11-07
### Improvements

- Bump Django Codebase to [v2.0.4](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
  - `assets` & `templates` moved to `apps` folder
- Adeed Gulp tooling for SCSS compilation

## [1.0.3] 2021-09-09
### Improvements & Fixes

- Bump Django Codebase to [v2.0.2](https://github.com/app-generator/boilerplate-code-django-dashboard/releases)
  - Dependencies update (all packages)
  - Use Django==3.2.6 (latest stable version)
  - Better Code formatting
  - Improved Files organization
  - Optimize imports
  - Docker Scripts Update 
- Tooling
  - SCSS compilation via Gulp
  - Update README with build instructions: `Recompile CSS` section     
- Fixes: 
  - Patch 500 Error when authenticated users access `admin` path (no slash at the end)
  - Patch: Update sidebar to reflect the current page 
  - Patch [#16](https://github.com/app-generator/boilerplate-code-django-dashboard/issues/16): Minor issue in Docker 

## [1.0.2] 2020-03-22
### Fixes 

- Bump Codebase: [Django Dashboard](https://github.com/app-generator/boilerplate-code-django-dashboard) v1.0.4
- Bump UI: [Jinja Datta PRO](https://github.com/app-generator/jinja-datta-able-pro) v1.0.2

## [1.0.1] 2020-05-30
### Bug fixing, Improvements
- Add CHANGELOG.md to track all changes
- Patch - Error-404.html not used in all contexts
- Update LICENSE file - added more information regarding the app usage

## [1.0.0] 2020-05-01
### Initial Release
