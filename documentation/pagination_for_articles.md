## Pagination for articles

---

1. Create include template

```python
{% include 'inc/pagination.html' %}
```

2. Create template
```html
{% block pagination %}
    {% if page_obj.has_other_pages %}
        <div class="pegination">
            <div class="nav-links">

                {% if page_obj.has_previous %}
                    <a class="page-numbers" href="?page={{ page_obj.previous_page_number }}"><i class="fa fa-angle-left"
                                                                                                aria-hidden="true"></i></a>
                {% endif %}

                {% for p in page_obj.paginator.page_range %}
                    {% if page_obj.number == p %}
                        <span class="page-numbers current">{{ p }}</span>
                    {% elif p > page_obj.number|add:-3 and p < page_obj.number|add:3 %}
                        <a class="page-numbers" href="?page={{ p }}">{{ p }}</a>
                    {% endif %}
                {% endfor %}

                {% if page_obj.has_next %}
                    <a class="page-numbers" href="?page={{ page_obj.next_page_number }}"><i class="fa fa-angle-right"
                                                                                            aria-hidden="true"></i></a>
                {% endif %}

            </div>
        </div>
    {% endif %}
{% endblock %}
```

3. for limited quantity pagination

`{% elif p > page_obj.number|add:-3 and p < page_obj.number|add:3 %}`