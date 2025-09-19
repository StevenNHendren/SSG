class HTMLNode():
    def __init__(self, tag: None, value: None, children: None, props: None):
        self.tag = tag #string representing HTML tag name (eg "p", "a", "h1", etc.)
        self.value = value #string representing value of the HTML tag (e.g. the text inside a paragraph)
        self.children = children #a list of HTMLNode objects representing the children of this node
        self.props = props #a dictionary of key-value pairs representing attributes of HTML tag
                            #link (<a> tag) might have {"href": "https://www.google.com"}
    
    def to_html(self):
        raise NotImplementedError

    def __repr__(self):
        retstring = ""
        if self.tag == None:
            retstring.append("tag: None\n")
        elif isinstance(self.tag, Str):
            retstring.append(f"tag: {self.tag}\n")
        if self.value == None:
            retstring.append("value: None\n")
        elif isinstance(self.value, Str):
            retstring.append(f"value: {self.value}\n")
        if self.children == None:
            retstring.append("children: None\n")
        else:
            retstring.append(f"children: {len(self.children)} members\n")
        if self.props == None:
            retstring.append("props: None\n")
        else:
            retstring.append(f"props: {self.props}\n")
        return retstring

    def props_to_html(self):
        ret = ""
        if self.props == None:
            return ret
        for k, v in self.props.items():
            ret.append(f" {k} {v}\n")
        return ret

class LeafNode(HTMLNode):

    def __init__(self, tag, value, props: None):
        super.__init__(tag, value, None, props)

    def to_html(self):
        if self.vaue == None:
            raise ValueError
        if self.tag == None:
           return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
