public: yes
tags: [javascript, ajax, script]
summary: |
  Cross Browser Ajax method.

Cross Browser Ajax
==================

Cross Browser Ajax method.

.. sourcecode:: javascript

    /**
     * IE 5.5+, Firefox, Opera, Chrome, Safari XHR object
     *
     * @param string url
     * @param object callback
     * @param mixed data
     * @param null x
     */
    function ajax(url, callback, data, x) {
        try {
            x = new (this.XMLHttpRequest || ActiveXObject)('MSXML2.XMLHTTP.3.0');
            x.open(data ? 'POST' : 'GET', url, 1);
            x.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
            x.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
            x.onreadystatechange = function () {
                x.readyState > 3 && callback && callback(x.responseText, x);
            };
            x.send(data)
        } catch (e) {
            window.console && console.log(e);
        }
    };