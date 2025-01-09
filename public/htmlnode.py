class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes will override this function.")

    def props_to_html(self) -> str:
        if len(self.props) == 0:
            return ""
        props_str = ""
        for x in self.props:
            props_str = props_str + f" {x}=\"{self.props[x]}\""
        return props_str
    
    def __repr__(self):
        msg = f'''
HTMLNode object:
tag: {self.tag}
value: {self.value}
props: {self.props}
children: {self.children}
'''
        return msg

class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None):
        if len(value) == 0:
            raise ValueError("'value' attribute required for LeafNode object")
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError("'value' attribute required for Leafnode object")
        if self.tag == None:
            return self.value
        start_tag = self.tag + self.props_to_html()
        return f"<{start_tag}>{self.value}</{self.tag}>"