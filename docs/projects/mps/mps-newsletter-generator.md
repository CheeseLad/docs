# MPS Newsletter Generator

*[GitHub Repository Link](https://github.com/CheeseLad/mps-newsletter-generator)*

A Python tool that automatically generates HTML email newsletters for DCUMPS (DCU Media Production Society) by processing HTML content from ZIP files and uploading images to external hosting.

## Features

- **Automatic Image Upload**: Uploads images to postimages.org for reliable hosting
- **Smart Caching**: Caches uploaded images to avoid re-uploading
- **Template System**: Uses Jinja2 templates for consistent newsletter formatting
- **Section Processing**: Automatically processes different newsletter sections (chairperson, events, etc.)
- **Social Media Integration**: Includes social media links and icons
- **Email-Ready Output**: Generates HTML files optimized for email clients

## Prerequisites

- Python 3.9+
- Internet connection (for image uploads)
- postimages.org account (for image hosting)

## Environment Setup

Create a `.env` file in the project root with your postimages.org credentials:

```env
POSTIMAGES_EMAIL=your_email@example.com
POSTIMAGES_PASSWORD=your_password
```

**Note**: Keep your `.env` file secure and never commit it to version control.

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your settings in `config.py`:
   - Update image mappings for different sections
   - Set social media links and icons
   - Ensure header images are in the `assets/header_images/` directory

## Usage

1. Prepare your newsletter content as an HTML file
2. Zip the HTML file and any images together
3. Run the generator:
   ```bash
   python main.py your_newsletter.zip
   ```
4. The tool will:
   - Extract the ZIP file
   - Upload new images to postimages.org
   - Process the HTML content
   - Generate a final newsletter file: `mps-email-YYYY-MM-DD.html`

## Configuration

### Image Mappings
Edit `config.py` to map section names to header images:
```python
image_mappings = {
    "logo": "./assets/header_images/1.png",
    "chairperson": "./assets/header_images/2.png",
    "events": "./assets/header_images/7.png",
    # ... more mappings
}
```

### Social Media Links
Configure social media links and icons:
```python
social_data = [
    {
        "social_link": "https://www.facebook.com/dcumps",
        "social_image": "./assets/icons/mc_facebook.png"
    },
    # ... more social links
]
```

## Output

The tool generates a single HTML file named `mps-email-YYYY-MM-DD.html` that contains:
- Responsive email layout
- Section-specific header images
- Processed content from your input HTML
- Social media footer with links
- Email-optimized styling

## Notes

- Images are cached in `image_cache.json` to avoid re-uploading
- Temporary directories are automatically cleaned up
- The tool handles Windows and Google Drive file system quirks
- All images are uploaded to postimages.org for reliable hosting

## Troubleshooting

- If image uploads fail, check your internet connection and postimages.org credentials
- Ensure your HTML file has proper section markers (`<p class="c...">`)
- Check that all referenced images exist in the ZIP file
  
## To-do:
- [ ] Replace <title> with the actual title from Google Docs
