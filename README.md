# scrapy-tabula-tt
Developing scrapy and tabula code to retrieve economic data about TT.

## 1. Basics of scrapy
### 1-1. Create project
```bash
scrapy startproject <project-name> [project-dir]
```
### 1-2. Create spyder
```bash
scrapy genspider [-t <template(crawl)>] <spyder-name> <target-domain>
```
### 1-3. Modify `<project>.py`, `items.py` and `settings.py`
<a href="https://note.nkmk.me/python-scrapy-tutorial/" target="_blank">Python, Scrapyの使い方（Webクローリング、スクレイピング）</a>

### 1-4. run crawler
```bash
scrapy crawl <spider-name> [-o <file-name or stdout:>] [-t <format(csv)> ] [--nolog]
```
`<spider-name>`はスパイダーのファイル名ではなくスパイダークラスの`name`で定義された名前。`genspider`で生成した場合はファイル名と`name`は同じになるが、自分でゼロから作成した場合は注意。

### 1-5. Debug
```bash
scrapy shell <url>
response.css('<CSS selector>').extract_first()
exit()
```
