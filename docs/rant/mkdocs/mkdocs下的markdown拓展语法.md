---
tags: "DocWriting"
---

# 0x01 mkdocs下的markdown拓展语法

摘录自：[Admonitions - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)

## Admonitions

### Usage

``` markdown
!!! note
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

> 1. allow nested
> 2. changing title

## Collapsible Blocks

### Usage

``` markdown
??? note

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.
```

> \???+ renders the block expanded

## Inline Blocks

### Usage

inline（靠左） & inline end（靠右）

``` markdown
!!! info inline end "Lorem ipsum"

    Lorem ipsum dolor sit amet, consectetur
    adipiscing elit. Nulla et euismod nulla.
    Curabitur feugiat, tortor non consequat
    finibus, justo purus auctor massa, nec
    semper lorem quam in massa.
```

## Annotation

### Usage

``` markdown 
Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
{ .annotate }

1.  :man_raising_hand: I'm an annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be expressed in Markdown.
```

> 1. allow nested inside annotations

## Content tabs

### usage

``` markdown
=== "Tab 1"

    Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.
    { .annotate }

    1.  :man_raising_hand: I'm an annotation!

=== "Tab 2"

    Phasellus posuere in sem ut cursus (1)
    { .annotate }

    1.  :woman_raising_hand: I'm an annotation as well!
```

## in everything else

### Usage

in some situation, the Attribue LIst don't work.That can use Markdown in Html.

``` markdown
<div class="annotate" markdown>

> Lorem ipsum dolor sit amet, (1) consectetur adipiscing elit.

</div>

1.  :man_raising_hand: I'm an annotation!
```

## Buttons

### Usage

``` markdown
[Subscribe to our newsletter](#){ .md-button}
```

> display a filled, primary button `.md-button--primary`

## Code Blocks

### Adding a title

````markdown
``` py title="bubble_sort.py"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```
````

### Adding Annotations

````yaml
``` yaml
theme:
  features:
    - content.code.annotate # (1)
```

1.  :man_raising_hand: I'm a code annotation! I can contain `code`, __formatted
    text__, images, ... basically anything that can be written in Markdown.
````

#### Stripping Comments

````yaml
``` yaml
# (1)!
```

1.  Look ma, less line noise!
````

### Adding line numbers

````markdown
``` py linenums="1"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```
````

### Highlingting Specific Lines

````markdown
``` py hl_lines="2 3"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```
````

> line counts start at 1

### Highlighting inline code blocks

``` markdown
The `#!python range()` function is used to generate a sequence of numbers.
```



### Embedding external files

````markdown
``` title=".browserslistrc"
--8<-- ".browserslistrc"
```
````

### Customization

[Code blocks - Material for MkDocs](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#customization)

## Data Tables
### Usage
=== "Data table"
``` markdown
| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |
```

| Method      | Description                          |
| ----------- | ------------------------------------ |
| `GET`       | :material-check:     Fetch resource  |
| `PUT`       | :material-check-all: Update resource |
| `DELETE`    | :material-close:     Delete resource |

#### Column alignment

=== "left"
    ```` markdown title="Data table, columns aligned to left"
    | Method      | Description                          |
    | :----------- | :------------------------------------ |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |
    ````
=== "center"
    ```` markdown title="Data table, columns aligned to left"
    | Method      | Description                          |
    | :-----------: | :------------------------------------: |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |
    ````
=== "right"
    ```` markdown title="Data table, columns aligned to left"
    | Method      | Description                          |
    | -----------: | ------------------------------------: |
    | `GET`       | :material-check:     Fetch resource  |
    | `PUT`       | :material-check-all: Update resource |
    | `DELETE`    | :material-close:     Delete resource |
    ````



## FootNotes

### Usage

``` markdown title="Text with footnote references"
Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]
```

Lorem ipsum[^1] dolor sit amet, consectetur adipiscing elit.[^2]

[^1]: Lorem ipsum dolor sit amet, consectetur adipiscing elit.
[^2]:
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
    nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
    massa, nec semper lorem quam in massa.

## Formatting

### Highlighting changes

``` markdown title="text with suggested changes"
Text can be {--deleted--} and replacement text {++added++}. This can also be
combined into {~~one~>a single~~} operation. {==Highlighting==} is also
possible {>>and comments can be added inline<<}.

{==

Formatting can also be applied to blocks by putting the opening and closing
tags on separate lines and adding new lines between the tags and the content.

==}
```

Text can be {--deleted--} and replacement text {++added++}. This can also be
combined into {~~one~>a single~~} operation. {==Highlighting==} is also
possible {>>and comments can be added inline<<}.

{==

Formatting can also be applied to blocks by putting the opening and closing
tags on separate lines and adding new lines between the tags and the content.

==}

### Highlight text

``` markdown title="Text with highlighting"
- ==This was marked (highlight)==
- ^^This was inserted (underline)^^
- ~~This was deleted (strikethrough)~~
```

- ==This was marked (highlight)==
- ^^This was inserted (underline)^^
- ~~This was deleted (strikethrough)~~

### Sub- and superscripts

``` markdown title="**Text with sub- and superscripts**"
- H~2~O
- A^T^A
```

- H~2~O
- A^T^A

### Adding keyboard keys

``` markdown title="keyboard keys"
++ctrl+alt+del++
```

++ctrl+alt+del++

## Grids

### Usage

#### Card Grid

``` markdown title="Card grid"
<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
```

<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

#### Another more complicate one

``` markdown title="card grid"
<div class="grid cards" markdown>

-   :material-clock-fast:{ .lg .middle } __Set up in 5 minutes__

    ---

    Install [`mkdocs-material`](#) with [`pip`](#) and get up
    and running in minutes

    [:octicons-arrow-right-24: Getting started](#)

-   :fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__

    ---

    Focus on your content and generate a responsive and searchable static site

    [:octicons-arrow-right-24: Reference](#)

-   :material-format-font:{ .lg .middle } __Made to measure__

    ---

    Change the colors, fonts, language, icons, logo and more with a few lines

    [:octicons-arrow-right-24: Customization](#)

-   :material-scale-balance:{ .lg .middle } __Open Source, MIT__

    ---

    Material for MkDocs is licensed under MIT and available on [GitHub]

    [:octicons-arrow-right-24: License](#)

</div>
```

<div class="grid cards" markdown>
-	:material-clock-fast:{.lg .middle } __Set up in 5 minutes__

	---
	
	Install [`mkdocs-material`](#)with [`pip`](#) and get up and running in minutes
	
	[:octicons-arrow-right-24: Getting Started](#)

-	:fontawesome-brands-markdown:{ .lg .middle } __It's just Markdown__
	
	---
	
	Focus on your content and generate a responsive and searchable static site
	
	[:octicons-arrow-right-24: Reference](#)
	
-	:material-format-font:{ .lg .middle } __Made to measure__
	
	---
	
	Change the colors, fonts, language, icons, logo, logo and more with a few lines
	
	[:octicons-arrow-right-24: Customization](#)
	
-	:material-scale-balance:{ .lg .middle } __Open Source, MIT__

	---
	
	Material for MkDocs is licensed under MIT and available on [GitHub](https://www.github.com)
	
	[:octicons-arrow-right-24: License](#)
	

</div>

#### Block syntax

``` markdown title="**Card grid, blocks**"
<div class="grid" markdown>

:fontawesome-brands-html5: __HTML__ for content and structure
{ .card }

:fontawesome-brands-js: __JavaScript__ for interactivity
{ .card }

:fontawesome-brands-css3: __CSS__ for text running out of boxes
{ .card }

> :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>
```
<div class="grid" markdown>

:fontawesome-brands-html5: __HTML__ for content and structure
{ .card }

:fontawesome-brands-js: __JavaScript__ for interactivity
{ .card }

:fontawesome-brands-css3: __CSS__ for text running out of boxes
{ .card }

> :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

#### Using generic grid 

````markdown title="Generic grid"
<div class="grid" markdown>

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Content tabs"
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

</div>
````

<div class="grid" markdown>

=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci

``` title="Content tabs"
=== "Unordered list"

    * Sed sagittis eleifend rutrum
    * Donec vitae suscipit est
    * Nulla tempor lobortis orci

=== "Ordered list"

    1. Sed sagittis eleifend rutrum
    2. Donec vitae suscipit est
    3. Nulla tempor lobortis orci
```

</div>

## Images

### Usage

#### Image alignment

=== "left"

	``` markdown title="Image, aligned to left"
	![Image title](https://dummyimage.com/600x400/eee/aaa){ align=left }
	```
	
	<div class="result" markdown>
	
	![Image title](https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–){ align=left width=300 }
	
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
	nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
	massa, nec semper lorem quam in massa.
	
	</div>

=== "Right"

	``` markdown title="Image, aligned to right"
	![Image title](https://dummyimage.com/600x400/eee/aaa){ align=right }
	```
	
	<div class="result" markdown>
	
	![Image title](https://dummyimage.com/600x400/f5f5f5/aaaaaa?text=–%20Image%20–){ align=left width=300 }
	
	Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et euismod
	nulla. Curabitur feugiat, tortor non consequat finibus, justo purus auctor
	massa, nec semper lorem quam in massa.
	
	</div>



#### Image captions

=== "Image with caption"
	
	``` markdown
	<figure markdown='span'>
		![Image title](https://dummyimage.com/600x400/){ width="300"}
		<figcaption>Image caption</figcation>
	</figure>
	```
	<div class="result" markdown>
	
	<figure markdown='span'>
		![Image title](https://dummyimage.com/600x400/){ width="300"}
		<figcaption>Image caption</figcation>
	</figure>
	
	</div>

#### Image lazy-loading
`![Image title](https://dummyimage.com/600x400/){ loading=lazy }`

## List

### Definition List

=== "Definition List"
	
	```markdown
	`Lorem ipsim dolor sit amet`
	
	:	Sed sagittis eleifend rutrum. Donec vitae suscipit est. Nullam tempus 
		tellus non sem sollicitudin, quis rutrum leo facilisis.
	
	`Cras arcu libero`
	
	:	Aliquam metus eros, pretium sed nulla venenatis, faucibus auctor ex. 
		Proin ut eros sed sapien ullamcorper consequat. Nunc ligula ante.
	
		Duis mollis est eget nibh volutpat, fermentum aliquet dui mollis. 
		Nam vulputate tincidunt fringilla. Nullam dignissim ultrices urna non auctor.
	
	```
	
	<div class="result" markdown>
	
	`Lorem ipsim dolor sit amet`
	
	:	Sed sagittis eleifend rutrum
	
	`Cras arcu libero`
	
	:	Aliquam metus eros, 
	
	</div>

### using task lists
=== "Task Lists"
    ```markdown title="TaskList"
    - [x] Lorem ipsum dolor sit amet,consectetur adipiscing elit
    - [ ] Vestibulum convallis sit amet nisi a tincidunt
    * [x] In hac habitasse platea dictumst
    * [x] In scelerisque nibh non dolor mollis congue sed et metus
    * [ ] Praesent sed risus massa
    - [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque
    ```
	
	<div class="result" markdown>
	
	- [x] Lorem ipsum dolor sit amet,consectetur adipiscing elit
	- [ ] Vestibulum convallis sit amet nisi a tincidunt
	* [x] In hac habitasse platea dictumst
	* [x] In scelerisque nibh non dolor mollis congue sed et metus
	* [ ] Praesent sed risus massa
	- [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque
	 	
	</div>

## Math

### Usage
#### Using block synatx
=== "block syntax"
	```markdown 
	$$
	\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
	$$
	```
	<div class="result" markdown>
	
	$$
	\cos x=\sum_{k=0}^{\infty}\frac{(-1)^k}{(2k)!}x^{2k}
	$$
	
	</div>

#### Using inline block syntax
=== "inline syntax"
	```markdown
	The homomorphism $f$ is injective if and only if its kernel is only the
	singleton set $e_G$, because otherwise $\exists a,b\in G$ with $a\neq b$ such that $f(a)=f(b)$.
	```
	
	<div class="result" markdown>
	
	The homomorphism $f$ is injective if and only if its kernel is only the singleton set $e_G$, because otherwise $\exists a,b\in G$ with $a\neq b$ such that $f(a)=f(b)$.
	
	</div>


## Tooltips
### Usage
#### Adding tooltips

=== "Link with tooltip, inline syntax"
	```markdown
	[Hover me](https://example.com "I'm a tooltip")
	```
	
	<div class="result" markdown>
	
	[Hover me](https://example.com "I'm a tooltip")
	
	</div>

#### with title

=== "Lnk with tooltip, reference syntax"
	```markdown
	
	:material-information-outline:{ title="Important information" }
	```
	
	<div class="result" markdown>
	
	:material-information-outline:{ title="Important information" }
	</div>

#### Adding abbreviations


#### Adding a glossary
The HTML specification is maintained by the W3C.
