# Changelog

All notable changes to Elm Offer Agent are documented in this file.

---

## v0.4.1 - Stability & UI improvements

### Added
- Dynamic version display on the website  
- Toast notification for copy action  
- Improved usage instructions  

### Changed
- Simplified UI and reduced instruction noise  
- Updated versioning system (build-based)  
- Improved build consistency across all variants  

### Fixed
- Cache issues with GitHub raw files (cache busting)  
- Incorrect version display in Light and Quick builds  

---

## v0.4.0 - Multi-build system

### Added
- Full / Light / Quick build variants  
- Build-specific output rules  
- Modular prompt architecture  
- Version suffix system (f / l / q)  

### Changed
- Prompt split into multiple modules  
- Build pipeline rewritten to support multiple outputs  

---

## v0.3.0 - Initial structured Elm

### Added
- Output structure enforcement  
- Compatibility checks (GPU, PSU, storage, etc.)  
- Debug & feedback system with error codes  
- Scoring system (compatibility & wishes match)  

---

## v0.2.0 - Expanded validation

### Added
- Advanced hardware compatibility checks  
- NVMe lane and PCIe conflict detection  
- GPU clearance and PSU validation  
- Improved customer analysis  

---

## v0.1.0 - Initial version

### Added
- Basic prompt for checking PC offers  
- Customer analysis and email generation  