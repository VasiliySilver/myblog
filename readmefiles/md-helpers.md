## MarkDown Helpers

---

1. Type texts

        *This text will be italic*
        _This will also be italic_
        
        **This text will be bold**
        __This will also be bold__
        
        _You **can** combine them_

*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_


2. Add dots

        * Item 1
        * Item 2
          * Item 2a
          * Item 2b

* Item 1
* Item 2
  * Item 2a
  * Item 2b
  
3. Add images

![GitHub Logo](img/2.png)
Format: ![Alt Text](url)

        ![GitHub Logo](img/2.png)
                  Format: ![Alt Text](url)


4. Links

http://github.com - automatic!
[GitHub](http://github.com)

        http://github.com - automatic!
        [GitHub](http://github.com)

5. Comments


As Kanye West said:

        > We're living the future so
        > the present is our past.

> We're living the future so
> the present is our past.

6. for simple examples of code use

        ``

I think you should use an
`<addr>` element here instead.

7. For hilghlight code examples



        ```javascript
        function fancyAlert(arg) {
          if(arg) {
            $.facebox({div:'#foo'})
          }
        }
        ```

```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

> or 4 spaces



    function fancyAlert(arg) {
      if(arg) {
        $.facebox({div:'#foo'})
      }
    }


8. For todo list

      - [x]
      - [ ]


- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item


9. For add table


    First Header | Second Header
    ------------ | -------------
    Content from cell 1 | Content from cell 2
    Content in the first column | Content in the second column

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column