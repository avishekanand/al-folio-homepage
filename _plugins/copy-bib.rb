Jekyll::Hooks.register :site, :post_write do |site|
  src  = File.join(site.source, '_bibliography', 'papers.bib')
  dest = File.join(site.dest, 'assets', 'bibliography', 'papers.bib')
  FileUtils.mkdir_p(File.dirname(dest))
  FileUtils.cp(src, dest)
end
