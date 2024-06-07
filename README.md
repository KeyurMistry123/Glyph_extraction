# README.md content
readme_content = """
# 📷 Glyph Extraction Project

Welcome to the **Glyph Extraction Project**! This project is designed to extract individual alphabet images from a computer font and save them as separate image files. It's a handy tool for anyone needing glyph images for various applications, such as creating custom datasets, font analysis, and more.

## ✨ Features

- 🎨 Extracts individual alphabet glyphs from a specified font.
- 🖼️ Saves each glyph as a separate image file.
- 🆎 Supports various font formats (e.g., TTF, OTF).
- 🛠️ Customizable output image size and format.
- 💻 Simple and easy-to-use command-line interface.

## 📚 Libraries Used

This project uses the following Python libraries:

- **Pillow**: The Python Imaging Library (PIL) is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats. Pillow is the friendly PIL fork and is used for creating and manipulating images in this project.

    Installation:
    \`\`\`bash
    pip install pillow
    \`\`\`

## 🤝 Contributing

We welcome contributions to improve this project! If you have suggestions, bug reports, or feature requests, please create an issue on GitHub. For code contributions, please fork the repository, create a new branch, and submit a pull request.

### 📝 Steps to Contribute

1. 🍴 Fork the repository.
2. 🌿 Create a new branch: \`git checkout -b my-feature-branch\`
3. 🛠️ Make your changes and commit them: \`git commit -m 'Add some feature'\`
4. 🔄 Push to the branch: \`git push origin my-feature-branch\`
5. 🔧 Submit a pull request.

## 🙏 Acknowledgements

Special thanks to the open-source community for their valuable contributions and resources.
"""

# Save README.md file
with open('README.md', 'w') as file:
    file.write(readme_content)


