# Shared Dependencies for Talk Decks

This directory contains shared resources for slide decks in the talks repository, reducing duplication and making maintenance easier.

## Directory Structure

- `css/`: Contains CSS files for reveal.js presentation framework
  - `reveal.css`: Main reveal.js styles
  - `reveal.scss`: SASS source files for reveal.js styles
  - `print/`: Print-specific styles
  - `theme/`: Theme files for presentations
  - `custom/`: Custom styling for presentations
    - `fonts.css`: Custom font styling
    - `layout.css`: Custom layout and spacing
- `js/`: JavaScript files
  - `reveal.js`: Main reveal.js script
- `lib/`: Third-party libraries
  - `css/`: Library CSS files including syntax highlighting
  - `js/`: Library JavaScript files
  - `font/`: Font files
- `plugin/`: Reveal.js plugins
  - `highlight/`: Code syntax highlighting
  - `markdown/`: Markdown support
  - `notes/`: Speaker notes

## Usage

To use these shared resources in your presentations, update the paths in your HTML files to point to this directory. Example:

```html
<!-- Instead of -->
<link rel="stylesheet" href="css/reveal.css">

<!-- Use -->
<link rel="stylesheet" href="../shared/css/reveal.css">

<!-- Add custom styling -->
<link rel="stylesheet" href="../shared/css/custom/fonts.css">
<link rel="stylesheet" href="../shared/css/custom/layout.css">
```

The path depends on your presentation's location relative to this shared directory. For presentations directly under the talks directory (like `talks/staypuft`), use `../shared/`. For presentations in subdirectories, adjust the path accordingly.

## Font Styling

To ensure consistent font styling across presentations:

1. Use the Google Fonts import for Source Sans Pro:
   ```html
   <link href='https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,300i,400,400i,600,600i,700,700i&display=swap' rel='stylesheet' type='text/css'>
   ```

2. Include the custom font styles:
   ```html
   <link rel="stylesheet" href="../shared/css/custom/fonts.css">
   ```

## Implementation Details

This shared directory was created to:
1. Reduce duplication across presentations
2. Simplify maintenance (update once, affects all presentations)
3. Standardize the appearance and behavior of presentations

For example implementations, see the `talks/staypuft` and `talks/request` presentations.