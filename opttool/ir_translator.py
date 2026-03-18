from ir import IRNode

GENERIC_TYPES = {
    "LOOP": "loop",
    "FUNCTION_CALL": "function_call",
    "FUNCTION_DEF": "function_def",
    "ATTRIBUTE_ACCESS": "attribute_access",
    "STRING_CONCAT": "string_concat",
    "EXCEPTION_HANDLER": "exception_handler",
    "GLOBAL_STATEMENT": "global_statement",
}

class IRTranslator:
    def __init__(self, rules):
        self.rules = rules

    def translate(self, node):
        node_type = self.get_generic_type(node.type)
        lineno = node.start_point[0] + 1
        children = [self.translate(child) for child in node.children]
        return IRNode(node_type or node.type, lineno, children)
    
    def get_generic_type(self, tree_sitter_type):
        for generic, mapped in GENERIC_TYPES.items():
            rule_list = getattr(self.rules, generic + "_TYPES",
                            getattr(self.rules, generic, []))
            if tree_sitter_type in rule_list:
                return mapped
        
        return None
    
