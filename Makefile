TIMESTAMP = `date +'%s'`
all: build css

build:
	@run-rstblog build
	@echo "Build HTML"

publish: git build css upload

css: css_minify css_timestamp

css_minify:
	@cssmin < _build/static/style.css > _build/static/style.min.css
	@mv _build/static/style.min.css _build/static/style.css
	@cssmin < _build/static/_pygments.css > _build/static/_pygments.min.css
	@mv _build/static/_pygments.min.css _build/static/_pygments.css
	@echo "Minify CSS"

css_timestamp:
	@find _build -type f -exec sed -i "s/\(link.*\)style.css/\\1style.css?${TIMESTAMP}/g" {} \;  
	@find _build -type f -exec sed -i "s/\(link.*\)_pygments.css/\\1_pygments.css?${TIMESTAMP}/g" {} \;
	@echo "Timestamp CSS"

upload:
	rsync -a _build/ ${user}@icron.org:${path}
	@echo "Done"

git:
	git pull
