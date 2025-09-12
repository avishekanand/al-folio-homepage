#!/usr/bin/env ruby
require 'kramdown'
require 'fileutils'

# Process graduated.md
puts "Processing graduated.md..."
graduated_content = File.read('_pages/graduated.md')
graduated_html = Kramdown::Document.new(graduated_content).to_html

# Create a simple HTML wrapper
html_template = <<~HTML
<!DOCTYPE html>
<html>
<head>
    <title>Graduated Students - Avishek Anand</title>
    <meta charset="utf-8">
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        a { color: #0066cc; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    #{graduated_html}
</body>
</html>
HTML

# Write to _site directory
FileUtils.mkdir_p('_site/people')
File.write('_site/people/graduated.html', html_template)

puts "Created _site/people/graduated.html with your updated content"
puts "Your changes include:"
puts "- Venktesh Viswananthan (now Asst. prof. in University of Stockholm)"
puts "- Lijun Lyu (now in Amazon)"
puts "- Abhijit Anand (now at Ambition-Mercedes)"
puts "- Maximilian Idahl (now at EllaMind)"
