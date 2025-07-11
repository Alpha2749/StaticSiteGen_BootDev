class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("This method should be implemented by child classes")
    
    def props_to_html(self):
        prop_string = " "
        for prop in self.props:
            prop_string += f" {prop}=\"{self.props[prop]}\""
    
    def __repr__(self):
        out_str = f"Tag: {self.tag}\nValue: {self.value}"
        out_str += f"Children: {self.children}\nProps: {self.props}"
        return out_str