class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ""
        if self.props:
            for prop in self.props:
                output += f' {prop}="{self.props[prop]}"'
        return output
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self,  value, tag=None, props=None):
        super().__init__(tag=tag, value=value, props=props)
        if value is None:
            raise ValueError

    def to_html(self):
        if self.tag is None:
            return f"{self.value}"
        elif self.props:
            return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        if self.tag is None:
            raise ValueError("tag is required in ParentNode")
        if self.children is None:
            raise ValueError("Child required for ParentNode")

    def to_html(self):

        current_node = f"<{self.tag}>"
        child_strings = ""
        for child in self.children:
            child_strings += child.to_html()
        return f"{current_node}{child_strings}</{self.tag}>"
            

