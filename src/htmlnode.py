class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("This method should be implemented by child classes")
    
    def props_to_html(self):
        prop_string = ""
        for prop in self.props:
            prop_string += f" {prop}=\"{self.props[prop]}\""
        return prop_string
    
    def __repr__(self):
        out_str = f"Tag: {self.tag}\nValue: {self.value}"
        out_str += f"Children: {self.children}\nProps: {self.props}"
        return out_str
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if not self.tag:
            return self.value
        propstring = ""
        if self.props:
            propstring = self.props_to_html()

        html_string = f"<{self.tag}{propstring}>{self.value}</{self.tag}>"
        return html_string

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have tags")
        if not self.children:
            raise ValueError("Missing children")
        propstring = ""
        if self.props:
            propstring = self.props_to_html()
        html_out = f"<{self.tag}{propstring}>"
        for child in self.children:
            html_out += child.to_html()
        html_out += f"</{self.tag}>"
        return html_out