## get-tags
[TOC]
### Tags cloud
- get all tags
- sidebar.py
```py
@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()
    return {"tags": tags}
```
### Representation tags
- create tags_tpl.html
- tags_tpl.html
```html
<div class="tags">
    <h2 class="sidebar-title">Tags</h2>
    {% for tag in tags %}
        <p><a href="{{ tag.get_absolute_url }}">{{  tag.title }}</a></p>
    {% endfor %}


</div>
```
### get tags in single
- use tag for tats
- single.html

```html
{% get_tags %}
```

### get absolute url for tags
- models.py
```py
    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})
```
