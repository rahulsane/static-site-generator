class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Child classes will override this function.")

    def props_to_html(self) -> str:
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
