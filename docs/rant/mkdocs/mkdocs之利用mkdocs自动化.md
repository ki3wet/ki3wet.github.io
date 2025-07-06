# 0x02 Document Automation
摘录自[Usage - mkdocstrings](https://mkdocstrings.github.io/usage/)

## 配置与安装

=== "mkdocs.yml"

	```yaml hl_lines="5 6"
	site_name: "My Library"
	
	theme:
		name: "material"
	watch:
		- src
	plugins:
	- search
	- mkdocstrings
	```

