# Generated from typeScript/TypeScriptParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TypeScriptParser import TypeScriptParser
else:
    from TypeScriptParser import TypeScriptParser

# This class defines a complete listener for a parse tree produced by TypeScriptParser.
class TypeScriptParserListener(ParseTreeListener):

    # Enter a parse tree produced by TypeScriptParser#initializer.
    def enterInitializer(self, ctx:TypeScriptParser.InitializerContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#initializer.
    def exitInitializer(self, ctx:TypeScriptParser.InitializerContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#bindingPattern.
    def enterBindingPattern(self, ctx:TypeScriptParser.BindingPatternContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#bindingPattern.
    def exitBindingPattern(self, ctx:TypeScriptParser.BindingPatternContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeParameters.
    def enterTypeParameters(self, ctx:TypeScriptParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeParameters.
    def exitTypeParameters(self, ctx:TypeScriptParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeParameterList.
    def enterTypeParameterList(self, ctx:TypeScriptParser.TypeParameterListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeParameterList.
    def exitTypeParameterList(self, ctx:TypeScriptParser.TypeParameterListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeParameter.
    def enterTypeParameter(self, ctx:TypeScriptParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeParameter.
    def exitTypeParameter(self, ctx:TypeScriptParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#constraint.
    def enterConstraint(self, ctx:TypeScriptParser.ConstraintContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#constraint.
    def exitConstraint(self, ctx:TypeScriptParser.ConstraintContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeArguments.
    def enterTypeArguments(self, ctx:TypeScriptParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeArguments.
    def exitTypeArguments(self, ctx:TypeScriptParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeArgumentList.
    def enterTypeArgumentList(self, ctx:TypeScriptParser.TypeArgumentListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeArgumentList.
    def exitTypeArgumentList(self, ctx:TypeScriptParser.TypeArgumentListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeArgument.
    def enterTypeArgument(self, ctx:TypeScriptParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeArgument.
    def exitTypeArgument(self, ctx:TypeScriptParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#type_.
    def enterType_(self, ctx:TypeScriptParser.Type_Context):
        pass

    # Exit a parse tree produced by TypeScriptParser#type_.
    def exitType_(self, ctx:TypeScriptParser.Type_Context):
        pass


    # Enter a parse tree produced by TypeScriptParser#Intersection.
    def enterIntersection(self, ctx:TypeScriptParser.IntersectionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#Intersection.
    def exitIntersection(self, ctx:TypeScriptParser.IntersectionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#Primary.
    def enterPrimary(self, ctx:TypeScriptParser.PrimaryContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#Primary.
    def exitPrimary(self, ctx:TypeScriptParser.PrimaryContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#Union.
    def enterUnion(self, ctx:TypeScriptParser.UnionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#Union.
    def exitUnion(self, ctx:TypeScriptParser.UnionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#RedefinitionOfType.
    def enterRedefinitionOfType(self, ctx:TypeScriptParser.RedefinitionOfTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#RedefinitionOfType.
    def exitRedefinitionOfType(self, ctx:TypeScriptParser.RedefinitionOfTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#PredefinedPrimType.
    def enterPredefinedPrimType(self, ctx:TypeScriptParser.PredefinedPrimTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#PredefinedPrimType.
    def exitPredefinedPrimType(self, ctx:TypeScriptParser.PredefinedPrimTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ArrayPrimType.
    def enterArrayPrimType(self, ctx:TypeScriptParser.ArrayPrimTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ArrayPrimType.
    def exitArrayPrimType(self, ctx:TypeScriptParser.ArrayPrimTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ParenthesizedPrimType.
    def enterParenthesizedPrimType(self, ctx:TypeScriptParser.ParenthesizedPrimTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ParenthesizedPrimType.
    def exitParenthesizedPrimType(self, ctx:TypeScriptParser.ParenthesizedPrimTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ThisPrimType.
    def enterThisPrimType(self, ctx:TypeScriptParser.ThisPrimTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ThisPrimType.
    def exitThisPrimType(self, ctx:TypeScriptParser.ThisPrimTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#TuplePrimType.
    def enterTuplePrimType(self, ctx:TypeScriptParser.TuplePrimTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#TuplePrimType.
    def exitTuplePrimType(self, ctx:TypeScriptParser.TuplePrimTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ObjectPrimType.
    def enterObjectPrimType(self, ctx:TypeScriptParser.ObjectPrimTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ObjectPrimType.
    def exitObjectPrimType(self, ctx:TypeScriptParser.ObjectPrimTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ReferencePrimType.
    def enterReferencePrimType(self, ctx:TypeScriptParser.ReferencePrimTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ReferencePrimType.
    def exitReferencePrimType(self, ctx:TypeScriptParser.ReferencePrimTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#QueryPrimType.
    def enterQueryPrimType(self, ctx:TypeScriptParser.QueryPrimTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#QueryPrimType.
    def exitQueryPrimType(self, ctx:TypeScriptParser.QueryPrimTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#predefinedType.
    def enterPredefinedType(self, ctx:TypeScriptParser.PredefinedTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#predefinedType.
    def exitPredefinedType(self, ctx:TypeScriptParser.PredefinedTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeReference.
    def enterTypeReference(self, ctx:TypeScriptParser.TypeReferenceContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeReference.
    def exitTypeReference(self, ctx:TypeScriptParser.TypeReferenceContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#nestedTypeGeneric.
    def enterNestedTypeGeneric(self, ctx:TypeScriptParser.NestedTypeGenericContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#nestedTypeGeneric.
    def exitNestedTypeGeneric(self, ctx:TypeScriptParser.NestedTypeGenericContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeGeneric.
    def enterTypeGeneric(self, ctx:TypeScriptParser.TypeGenericContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeGeneric.
    def exitTypeGeneric(self, ctx:TypeScriptParser.TypeGenericContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeIncludeGeneric.
    def enterTypeIncludeGeneric(self, ctx:TypeScriptParser.TypeIncludeGenericContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeIncludeGeneric.
    def exitTypeIncludeGeneric(self, ctx:TypeScriptParser.TypeIncludeGenericContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeName.
    def enterTypeName(self, ctx:TypeScriptParser.TypeNameContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeName.
    def exitTypeName(self, ctx:TypeScriptParser.TypeNameContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#objectType.
    def enterObjectType(self, ctx:TypeScriptParser.ObjectTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#objectType.
    def exitObjectType(self, ctx:TypeScriptParser.ObjectTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeBody.
    def enterTypeBody(self, ctx:TypeScriptParser.TypeBodyContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeBody.
    def exitTypeBody(self, ctx:TypeScriptParser.TypeBodyContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeMemberList.
    def enterTypeMemberList(self, ctx:TypeScriptParser.TypeMemberListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeMemberList.
    def exitTypeMemberList(self, ctx:TypeScriptParser.TypeMemberListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeMember.
    def enterTypeMember(self, ctx:TypeScriptParser.TypeMemberContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeMember.
    def exitTypeMember(self, ctx:TypeScriptParser.TypeMemberContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#arrayType.
    def enterArrayType(self, ctx:TypeScriptParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#arrayType.
    def exitArrayType(self, ctx:TypeScriptParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#tupleType.
    def enterTupleType(self, ctx:TypeScriptParser.TupleTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#tupleType.
    def exitTupleType(self, ctx:TypeScriptParser.TupleTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#tupleElementTypes.
    def enterTupleElementTypes(self, ctx:TypeScriptParser.TupleElementTypesContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#tupleElementTypes.
    def exitTupleElementTypes(self, ctx:TypeScriptParser.TupleElementTypesContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#functionType.
    def enterFunctionType(self, ctx:TypeScriptParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#functionType.
    def exitFunctionType(self, ctx:TypeScriptParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#constructorType.
    def enterConstructorType(self, ctx:TypeScriptParser.ConstructorTypeContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#constructorType.
    def exitConstructorType(self, ctx:TypeScriptParser.ConstructorTypeContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeQuery.
    def enterTypeQuery(self, ctx:TypeScriptParser.TypeQueryContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeQuery.
    def exitTypeQuery(self, ctx:TypeScriptParser.TypeQueryContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeQueryExpression.
    def enterTypeQueryExpression(self, ctx:TypeScriptParser.TypeQueryExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeQueryExpression.
    def exitTypeQueryExpression(self, ctx:TypeScriptParser.TypeQueryExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#propertySignatur.
    def enterPropertySignatur(self, ctx:TypeScriptParser.PropertySignaturContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#propertySignatur.
    def exitPropertySignatur(self, ctx:TypeScriptParser.PropertySignaturContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeAnnotation.
    def enterTypeAnnotation(self, ctx:TypeScriptParser.TypeAnnotationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeAnnotation.
    def exitTypeAnnotation(self, ctx:TypeScriptParser.TypeAnnotationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#callSignature.
    def enterCallSignature(self, ctx:TypeScriptParser.CallSignatureContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#callSignature.
    def exitCallSignature(self, ctx:TypeScriptParser.CallSignatureContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#parameterList.
    def enterParameterList(self, ctx:TypeScriptParser.ParameterListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#parameterList.
    def exitParameterList(self, ctx:TypeScriptParser.ParameterListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#requiredParameterList.
    def enterRequiredParameterList(self, ctx:TypeScriptParser.RequiredParameterListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#requiredParameterList.
    def exitRequiredParameterList(self, ctx:TypeScriptParser.RequiredParameterListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#parameter.
    def enterParameter(self, ctx:TypeScriptParser.ParameterContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#parameter.
    def exitParameter(self, ctx:TypeScriptParser.ParameterContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#optionalParameter.
    def enterOptionalParameter(self, ctx:TypeScriptParser.OptionalParameterContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#optionalParameter.
    def exitOptionalParameter(self, ctx:TypeScriptParser.OptionalParameterContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#restParameter.
    def enterRestParameter(self, ctx:TypeScriptParser.RestParameterContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#restParameter.
    def exitRestParameter(self, ctx:TypeScriptParser.RestParameterContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#requiredParameter.
    def enterRequiredParameter(self, ctx:TypeScriptParser.RequiredParameterContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#requiredParameter.
    def exitRequiredParameter(self, ctx:TypeScriptParser.RequiredParameterContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#accessibilityModifier.
    def enterAccessibilityModifier(self, ctx:TypeScriptParser.AccessibilityModifierContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#accessibilityModifier.
    def exitAccessibilityModifier(self, ctx:TypeScriptParser.AccessibilityModifierContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#identifierOrPattern.
    def enterIdentifierOrPattern(self, ctx:TypeScriptParser.IdentifierOrPatternContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#identifierOrPattern.
    def exitIdentifierOrPattern(self, ctx:TypeScriptParser.IdentifierOrPatternContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#constructSignature.
    def enterConstructSignature(self, ctx:TypeScriptParser.ConstructSignatureContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#constructSignature.
    def exitConstructSignature(self, ctx:TypeScriptParser.ConstructSignatureContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#indexSignature.
    def enterIndexSignature(self, ctx:TypeScriptParser.IndexSignatureContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#indexSignature.
    def exitIndexSignature(self, ctx:TypeScriptParser.IndexSignatureContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#methodSignature.
    def enterMethodSignature(self, ctx:TypeScriptParser.MethodSignatureContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#methodSignature.
    def exitMethodSignature(self, ctx:TypeScriptParser.MethodSignatureContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#typeAliasDeclaration.
    def enterTypeAliasDeclaration(self, ctx:TypeScriptParser.TypeAliasDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#typeAliasDeclaration.
    def exitTypeAliasDeclaration(self, ctx:TypeScriptParser.TypeAliasDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:TypeScriptParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:TypeScriptParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:TypeScriptParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:TypeScriptParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#interfaceExtendsClause.
    def enterInterfaceExtendsClause(self, ctx:TypeScriptParser.InterfaceExtendsClauseContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#interfaceExtendsClause.
    def exitInterfaceExtendsClause(self, ctx:TypeScriptParser.InterfaceExtendsClauseContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#classOrInterfaceTypeList.
    def enterClassOrInterfaceTypeList(self, ctx:TypeScriptParser.ClassOrInterfaceTypeListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#classOrInterfaceTypeList.
    def exitClassOrInterfaceTypeList(self, ctx:TypeScriptParser.ClassOrInterfaceTypeListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:TypeScriptParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:TypeScriptParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#enumBody.
    def enterEnumBody(self, ctx:TypeScriptParser.EnumBodyContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#enumBody.
    def exitEnumBody(self, ctx:TypeScriptParser.EnumBodyContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#enumMemberList.
    def enterEnumMemberList(self, ctx:TypeScriptParser.EnumMemberListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#enumMemberList.
    def exitEnumMemberList(self, ctx:TypeScriptParser.EnumMemberListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#enumMember.
    def enterEnumMember(self, ctx:TypeScriptParser.EnumMemberContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#enumMember.
    def exitEnumMember(self, ctx:TypeScriptParser.EnumMemberContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#namespaceDeclaration.
    def enterNamespaceDeclaration(self, ctx:TypeScriptParser.NamespaceDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#namespaceDeclaration.
    def exitNamespaceDeclaration(self, ctx:TypeScriptParser.NamespaceDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#namespaceName.
    def enterNamespaceName(self, ctx:TypeScriptParser.NamespaceNameContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#namespaceName.
    def exitNamespaceName(self, ctx:TypeScriptParser.NamespaceNameContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#importAliasDeclaration.
    def enterImportAliasDeclaration(self, ctx:TypeScriptParser.ImportAliasDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#importAliasDeclaration.
    def exitImportAliasDeclaration(self, ctx:TypeScriptParser.ImportAliasDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#decoratorList.
    def enterDecoratorList(self, ctx:TypeScriptParser.DecoratorListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#decoratorList.
    def exitDecoratorList(self, ctx:TypeScriptParser.DecoratorListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#decorator.
    def enterDecorator(self, ctx:TypeScriptParser.DecoratorContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#decorator.
    def exitDecorator(self, ctx:TypeScriptParser.DecoratorContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#decoratorMemberExpression.
    def enterDecoratorMemberExpression(self, ctx:TypeScriptParser.DecoratorMemberExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#decoratorMemberExpression.
    def exitDecoratorMemberExpression(self, ctx:TypeScriptParser.DecoratorMemberExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#decoratorCallExpression.
    def enterDecoratorCallExpression(self, ctx:TypeScriptParser.DecoratorCallExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#decoratorCallExpression.
    def exitDecoratorCallExpression(self, ctx:TypeScriptParser.DecoratorCallExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#program.
    def enterProgram(self, ctx:TypeScriptParser.ProgramContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#program.
    def exitProgram(self, ctx:TypeScriptParser.ProgramContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#sourceElement.
    def enterSourceElement(self, ctx:TypeScriptParser.SourceElementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#sourceElement.
    def exitSourceElement(self, ctx:TypeScriptParser.SourceElementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#statement.
    def enterStatement(self, ctx:TypeScriptParser.StatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#statement.
    def exitStatement(self, ctx:TypeScriptParser.StatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#block.
    def enterBlock(self, ctx:TypeScriptParser.BlockContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#block.
    def exitBlock(self, ctx:TypeScriptParser.BlockContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#statementList.
    def enterStatementList(self, ctx:TypeScriptParser.StatementListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#statementList.
    def exitStatementList(self, ctx:TypeScriptParser.StatementListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#abstractDeclaration.
    def enterAbstractDeclaration(self, ctx:TypeScriptParser.AbstractDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#abstractDeclaration.
    def exitAbstractDeclaration(self, ctx:TypeScriptParser.AbstractDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#importStatement.
    def enterImportStatement(self, ctx:TypeScriptParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#importStatement.
    def exitImportStatement(self, ctx:TypeScriptParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#fromBlock.
    def enterFromBlock(self, ctx:TypeScriptParser.FromBlockContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#fromBlock.
    def exitFromBlock(self, ctx:TypeScriptParser.FromBlockContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#multipleImportStatement.
    def enterMultipleImportStatement(self, ctx:TypeScriptParser.MultipleImportStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#multipleImportStatement.
    def exitMultipleImportStatement(self, ctx:TypeScriptParser.MultipleImportStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#exportStatement.
    def enterExportStatement(self, ctx:TypeScriptParser.ExportStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#exportStatement.
    def exitExportStatement(self, ctx:TypeScriptParser.ExportStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#variableStatement.
    def enterVariableStatement(self, ctx:TypeScriptParser.VariableStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#variableStatement.
    def exitVariableStatement(self, ctx:TypeScriptParser.VariableStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#variableDeclarationList.
    def enterVariableDeclarationList(self, ctx:TypeScriptParser.VariableDeclarationListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#variableDeclarationList.
    def exitVariableDeclarationList(self, ctx:TypeScriptParser.VariableDeclarationListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:TypeScriptParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:TypeScriptParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#emptyStatement.
    def enterEmptyStatement(self, ctx:TypeScriptParser.EmptyStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#emptyStatement.
    def exitEmptyStatement(self, ctx:TypeScriptParser.EmptyStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#expressionStatement.
    def enterExpressionStatement(self, ctx:TypeScriptParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#expressionStatement.
    def exitExpressionStatement(self, ctx:TypeScriptParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ifStatement.
    def enterIfStatement(self, ctx:TypeScriptParser.IfStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ifStatement.
    def exitIfStatement(self, ctx:TypeScriptParser.IfStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#DoStatement.
    def enterDoStatement(self, ctx:TypeScriptParser.DoStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#DoStatement.
    def exitDoStatement(self, ctx:TypeScriptParser.DoStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#WhileStatement.
    def enterWhileStatement(self, ctx:TypeScriptParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#WhileStatement.
    def exitWhileStatement(self, ctx:TypeScriptParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ForStatement.
    def enterForStatement(self, ctx:TypeScriptParser.ForStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ForStatement.
    def exitForStatement(self, ctx:TypeScriptParser.ForStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ForVarStatement.
    def enterForVarStatement(self, ctx:TypeScriptParser.ForVarStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ForVarStatement.
    def exitForVarStatement(self, ctx:TypeScriptParser.ForVarStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ForInStatement.
    def enterForInStatement(self, ctx:TypeScriptParser.ForInStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ForInStatement.
    def exitForInStatement(self, ctx:TypeScriptParser.ForInStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ForVarInStatement.
    def enterForVarInStatement(self, ctx:TypeScriptParser.ForVarInStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ForVarInStatement.
    def exitForVarInStatement(self, ctx:TypeScriptParser.ForVarInStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#varModifier.
    def enterVarModifier(self, ctx:TypeScriptParser.VarModifierContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#varModifier.
    def exitVarModifier(self, ctx:TypeScriptParser.VarModifierContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#continueStatement.
    def enterContinueStatement(self, ctx:TypeScriptParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#continueStatement.
    def exitContinueStatement(self, ctx:TypeScriptParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#breakStatement.
    def enterBreakStatement(self, ctx:TypeScriptParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#breakStatement.
    def exitBreakStatement(self, ctx:TypeScriptParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#returnStatement.
    def enterReturnStatement(self, ctx:TypeScriptParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#returnStatement.
    def exitReturnStatement(self, ctx:TypeScriptParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#yieldStatement.
    def enterYieldStatement(self, ctx:TypeScriptParser.YieldStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#yieldStatement.
    def exitYieldStatement(self, ctx:TypeScriptParser.YieldStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#withStatement.
    def enterWithStatement(self, ctx:TypeScriptParser.WithStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#withStatement.
    def exitWithStatement(self, ctx:TypeScriptParser.WithStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#switchStatement.
    def enterSwitchStatement(self, ctx:TypeScriptParser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#switchStatement.
    def exitSwitchStatement(self, ctx:TypeScriptParser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#caseBlock.
    def enterCaseBlock(self, ctx:TypeScriptParser.CaseBlockContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#caseBlock.
    def exitCaseBlock(self, ctx:TypeScriptParser.CaseBlockContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#caseClauses.
    def enterCaseClauses(self, ctx:TypeScriptParser.CaseClausesContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#caseClauses.
    def exitCaseClauses(self, ctx:TypeScriptParser.CaseClausesContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#caseClause.
    def enterCaseClause(self, ctx:TypeScriptParser.CaseClauseContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#caseClause.
    def exitCaseClause(self, ctx:TypeScriptParser.CaseClauseContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#defaultClause.
    def enterDefaultClause(self, ctx:TypeScriptParser.DefaultClauseContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#defaultClause.
    def exitDefaultClause(self, ctx:TypeScriptParser.DefaultClauseContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#labelledStatement.
    def enterLabelledStatement(self, ctx:TypeScriptParser.LabelledStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#labelledStatement.
    def exitLabelledStatement(self, ctx:TypeScriptParser.LabelledStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#throwStatement.
    def enterThrowStatement(self, ctx:TypeScriptParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#throwStatement.
    def exitThrowStatement(self, ctx:TypeScriptParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#tryStatement.
    def enterTryStatement(self, ctx:TypeScriptParser.TryStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#tryStatement.
    def exitTryStatement(self, ctx:TypeScriptParser.TryStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#catchProduction.
    def enterCatchProduction(self, ctx:TypeScriptParser.CatchProductionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#catchProduction.
    def exitCatchProduction(self, ctx:TypeScriptParser.CatchProductionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#finallyProduction.
    def enterFinallyProduction(self, ctx:TypeScriptParser.FinallyProductionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#finallyProduction.
    def exitFinallyProduction(self, ctx:TypeScriptParser.FinallyProductionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#debuggerStatement.
    def enterDebuggerStatement(self, ctx:TypeScriptParser.DebuggerStatementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#debuggerStatement.
    def exitDebuggerStatement(self, ctx:TypeScriptParser.DebuggerStatementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:TypeScriptParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:TypeScriptParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#classDeclaration.
    def enterClassDeclaration(self, ctx:TypeScriptParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#classDeclaration.
    def exitClassDeclaration(self, ctx:TypeScriptParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#classHeritage.
    def enterClassHeritage(self, ctx:TypeScriptParser.ClassHeritageContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#classHeritage.
    def exitClassHeritage(self, ctx:TypeScriptParser.ClassHeritageContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#classTail.
    def enterClassTail(self, ctx:TypeScriptParser.ClassTailContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#classTail.
    def exitClassTail(self, ctx:TypeScriptParser.ClassTailContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#classExtendsClause.
    def enterClassExtendsClause(self, ctx:TypeScriptParser.ClassExtendsClauseContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#classExtendsClause.
    def exitClassExtendsClause(self, ctx:TypeScriptParser.ClassExtendsClauseContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#implementsClause.
    def enterImplementsClause(self, ctx:TypeScriptParser.ImplementsClauseContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#implementsClause.
    def exitImplementsClause(self, ctx:TypeScriptParser.ImplementsClauseContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#classElement.
    def enterClassElement(self, ctx:TypeScriptParser.ClassElementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#classElement.
    def exitClassElement(self, ctx:TypeScriptParser.ClassElementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#PropertyDeclarationExpression.
    def enterPropertyDeclarationExpression(self, ctx:TypeScriptParser.PropertyDeclarationExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#PropertyDeclarationExpression.
    def exitPropertyDeclarationExpression(self, ctx:TypeScriptParser.PropertyDeclarationExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#MethodDeclarationExpression.
    def enterMethodDeclarationExpression(self, ctx:TypeScriptParser.MethodDeclarationExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#MethodDeclarationExpression.
    def exitMethodDeclarationExpression(self, ctx:TypeScriptParser.MethodDeclarationExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#GetterSetterDeclarationExpression.
    def enterGetterSetterDeclarationExpression(self, ctx:TypeScriptParser.GetterSetterDeclarationExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#GetterSetterDeclarationExpression.
    def exitGetterSetterDeclarationExpression(self, ctx:TypeScriptParser.GetterSetterDeclarationExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#AbstractMemberDeclaration.
    def enterAbstractMemberDeclaration(self, ctx:TypeScriptParser.AbstractMemberDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#AbstractMemberDeclaration.
    def exitAbstractMemberDeclaration(self, ctx:TypeScriptParser.AbstractMemberDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#propertyMemberBase.
    def enterPropertyMemberBase(self, ctx:TypeScriptParser.PropertyMemberBaseContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#propertyMemberBase.
    def exitPropertyMemberBase(self, ctx:TypeScriptParser.PropertyMemberBaseContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#indexMemberDeclaration.
    def enterIndexMemberDeclaration(self, ctx:TypeScriptParser.IndexMemberDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#indexMemberDeclaration.
    def exitIndexMemberDeclaration(self, ctx:TypeScriptParser.IndexMemberDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#generatorMethod.
    def enterGeneratorMethod(self, ctx:TypeScriptParser.GeneratorMethodContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#generatorMethod.
    def exitGeneratorMethod(self, ctx:TypeScriptParser.GeneratorMethodContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#generatorFunctionDeclaration.
    def enterGeneratorFunctionDeclaration(self, ctx:TypeScriptParser.GeneratorFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#generatorFunctionDeclaration.
    def exitGeneratorFunctionDeclaration(self, ctx:TypeScriptParser.GeneratorFunctionDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#generatorBlock.
    def enterGeneratorBlock(self, ctx:TypeScriptParser.GeneratorBlockContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#generatorBlock.
    def exitGeneratorBlock(self, ctx:TypeScriptParser.GeneratorBlockContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#generatorDefinition.
    def enterGeneratorDefinition(self, ctx:TypeScriptParser.GeneratorDefinitionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#generatorDefinition.
    def exitGeneratorDefinition(self, ctx:TypeScriptParser.GeneratorDefinitionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#iteratorBlock.
    def enterIteratorBlock(self, ctx:TypeScriptParser.IteratorBlockContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#iteratorBlock.
    def exitIteratorBlock(self, ctx:TypeScriptParser.IteratorBlockContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#iteratorDefinition.
    def enterIteratorDefinition(self, ctx:TypeScriptParser.IteratorDefinitionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#iteratorDefinition.
    def exitIteratorDefinition(self, ctx:TypeScriptParser.IteratorDefinitionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#formalParameterList.
    def enterFormalParameterList(self, ctx:TypeScriptParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#formalParameterList.
    def exitFormalParameterList(self, ctx:TypeScriptParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#formalParameterArg.
    def enterFormalParameterArg(self, ctx:TypeScriptParser.FormalParameterArgContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#formalParameterArg.
    def exitFormalParameterArg(self, ctx:TypeScriptParser.FormalParameterArgContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#lastFormalParameterArg.
    def enterLastFormalParameterArg(self, ctx:TypeScriptParser.LastFormalParameterArgContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#lastFormalParameterArg.
    def exitLastFormalParameterArg(self, ctx:TypeScriptParser.LastFormalParameterArgContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#functionBody.
    def enterFunctionBody(self, ctx:TypeScriptParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#functionBody.
    def exitFunctionBody(self, ctx:TypeScriptParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#sourceElements.
    def enterSourceElements(self, ctx:TypeScriptParser.SourceElementsContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#sourceElements.
    def exitSourceElements(self, ctx:TypeScriptParser.SourceElementsContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#arrayLiteral.
    def enterArrayLiteral(self, ctx:TypeScriptParser.ArrayLiteralContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#arrayLiteral.
    def exitArrayLiteral(self, ctx:TypeScriptParser.ArrayLiteralContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#elementList.
    def enterElementList(self, ctx:TypeScriptParser.ElementListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#elementList.
    def exitElementList(self, ctx:TypeScriptParser.ElementListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#arrayElement.
    def enterArrayElement(self, ctx:TypeScriptParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#arrayElement.
    def exitArrayElement(self, ctx:TypeScriptParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#objectLiteral.
    def enterObjectLiteral(self, ctx:TypeScriptParser.ObjectLiteralContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#objectLiteral.
    def exitObjectLiteral(self, ctx:TypeScriptParser.ObjectLiteralContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#PropertyExpressionAssignment.
    def enterPropertyExpressionAssignment(self, ctx:TypeScriptParser.PropertyExpressionAssignmentContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#PropertyExpressionAssignment.
    def exitPropertyExpressionAssignment(self, ctx:TypeScriptParser.PropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ComputedPropertyExpressionAssignment.
    def enterComputedPropertyExpressionAssignment(self, ctx:TypeScriptParser.ComputedPropertyExpressionAssignmentContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ComputedPropertyExpressionAssignment.
    def exitComputedPropertyExpressionAssignment(self, ctx:TypeScriptParser.ComputedPropertyExpressionAssignmentContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#PropertyGetter.
    def enterPropertyGetter(self, ctx:TypeScriptParser.PropertyGetterContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#PropertyGetter.
    def exitPropertyGetter(self, ctx:TypeScriptParser.PropertyGetterContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#PropertySetter.
    def enterPropertySetter(self, ctx:TypeScriptParser.PropertySetterContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#PropertySetter.
    def exitPropertySetter(self, ctx:TypeScriptParser.PropertySetterContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#MethodProperty.
    def enterMethodProperty(self, ctx:TypeScriptParser.MethodPropertyContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#MethodProperty.
    def exitMethodProperty(self, ctx:TypeScriptParser.MethodPropertyContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#PropertyShorthand.
    def enterPropertyShorthand(self, ctx:TypeScriptParser.PropertyShorthandContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#PropertyShorthand.
    def exitPropertyShorthand(self, ctx:TypeScriptParser.PropertyShorthandContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#RestParameterInObject.
    def enterRestParameterInObject(self, ctx:TypeScriptParser.RestParameterInObjectContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#RestParameterInObject.
    def exitRestParameterInObject(self, ctx:TypeScriptParser.RestParameterInObjectContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#getAccessor.
    def enterGetAccessor(self, ctx:TypeScriptParser.GetAccessorContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#getAccessor.
    def exitGetAccessor(self, ctx:TypeScriptParser.GetAccessorContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#setAccessor.
    def enterSetAccessor(self, ctx:TypeScriptParser.SetAccessorContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#setAccessor.
    def exitSetAccessor(self, ctx:TypeScriptParser.SetAccessorContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#propertyName.
    def enterPropertyName(self, ctx:TypeScriptParser.PropertyNameContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#propertyName.
    def exitPropertyName(self, ctx:TypeScriptParser.PropertyNameContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#arguments.
    def enterArguments(self, ctx:TypeScriptParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#arguments.
    def exitArguments(self, ctx:TypeScriptParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#argumentList.
    def enterArgumentList(self, ctx:TypeScriptParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#argumentList.
    def exitArgumentList(self, ctx:TypeScriptParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#argument.
    def enterArgument(self, ctx:TypeScriptParser.ArgumentContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#argument.
    def exitArgument(self, ctx:TypeScriptParser.ArgumentContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#expressionSequence.
    def enterExpressionSequence(self, ctx:TypeScriptParser.ExpressionSequenceContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#expressionSequence.
    def exitExpressionSequence(self, ctx:TypeScriptParser.ExpressionSequenceContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#functionExpressionDeclaration.
    def enterFunctionExpressionDeclaration(self, ctx:TypeScriptParser.FunctionExpressionDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#functionExpressionDeclaration.
    def exitFunctionExpressionDeclaration(self, ctx:TypeScriptParser.FunctionExpressionDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#TemplateStringExpression.
    def enterTemplateStringExpression(self, ctx:TypeScriptParser.TemplateStringExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#TemplateStringExpression.
    def exitTemplateStringExpression(self, ctx:TypeScriptParser.TemplateStringExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#TernaryExpression.
    def enterTernaryExpression(self, ctx:TypeScriptParser.TernaryExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#TernaryExpression.
    def exitTernaryExpression(self, ctx:TypeScriptParser.TernaryExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#LogicalAndExpression.
    def enterLogicalAndExpression(self, ctx:TypeScriptParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#LogicalAndExpression.
    def exitLogicalAndExpression(self, ctx:TypeScriptParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#GeneratorsExpression.
    def enterGeneratorsExpression(self, ctx:TypeScriptParser.GeneratorsExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#GeneratorsExpression.
    def exitGeneratorsExpression(self, ctx:TypeScriptParser.GeneratorsExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#PreIncrementExpression.
    def enterPreIncrementExpression(self, ctx:TypeScriptParser.PreIncrementExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#PreIncrementExpression.
    def exitPreIncrementExpression(self, ctx:TypeScriptParser.PreIncrementExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ObjectLiteralExpression.
    def enterObjectLiteralExpression(self, ctx:TypeScriptParser.ObjectLiteralExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ObjectLiteralExpression.
    def exitObjectLiteralExpression(self, ctx:TypeScriptParser.ObjectLiteralExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#InExpression.
    def enterInExpression(self, ctx:TypeScriptParser.InExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#InExpression.
    def exitInExpression(self, ctx:TypeScriptParser.InExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#LogicalOrExpression.
    def enterLogicalOrExpression(self, ctx:TypeScriptParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#LogicalOrExpression.
    def exitLogicalOrExpression(self, ctx:TypeScriptParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#GenericTypes.
    def enterGenericTypes(self, ctx:TypeScriptParser.GenericTypesContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#GenericTypes.
    def exitGenericTypes(self, ctx:TypeScriptParser.GenericTypesContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#NotExpression.
    def enterNotExpression(self, ctx:TypeScriptParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#NotExpression.
    def exitNotExpression(self, ctx:TypeScriptParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#PreDecreaseExpression.
    def enterPreDecreaseExpression(self, ctx:TypeScriptParser.PreDecreaseExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#PreDecreaseExpression.
    def exitPreDecreaseExpression(self, ctx:TypeScriptParser.PreDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ArgumentsExpression.
    def enterArgumentsExpression(self, ctx:TypeScriptParser.ArgumentsExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ArgumentsExpression.
    def exitArgumentsExpression(self, ctx:TypeScriptParser.ArgumentsExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ThisExpression.
    def enterThisExpression(self, ctx:TypeScriptParser.ThisExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ThisExpression.
    def exitThisExpression(self, ctx:TypeScriptParser.ThisExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#FunctionExpression.
    def enterFunctionExpression(self, ctx:TypeScriptParser.FunctionExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#FunctionExpression.
    def exitFunctionExpression(self, ctx:TypeScriptParser.FunctionExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#UnaryMinusExpression.
    def enterUnaryMinusExpression(self, ctx:TypeScriptParser.UnaryMinusExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#UnaryMinusExpression.
    def exitUnaryMinusExpression(self, ctx:TypeScriptParser.UnaryMinusExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#AssignmentExpression.
    def enterAssignmentExpression(self, ctx:TypeScriptParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#AssignmentExpression.
    def exitAssignmentExpression(self, ctx:TypeScriptParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#PostDecreaseExpression.
    def enterPostDecreaseExpression(self, ctx:TypeScriptParser.PostDecreaseExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#PostDecreaseExpression.
    def exitPostDecreaseExpression(self, ctx:TypeScriptParser.PostDecreaseExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#TypeofExpression.
    def enterTypeofExpression(self, ctx:TypeScriptParser.TypeofExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#TypeofExpression.
    def exitTypeofExpression(self, ctx:TypeScriptParser.TypeofExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#InstanceofExpression.
    def enterInstanceofExpression(self, ctx:TypeScriptParser.InstanceofExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#InstanceofExpression.
    def exitInstanceofExpression(self, ctx:TypeScriptParser.InstanceofExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#UnaryPlusExpression.
    def enterUnaryPlusExpression(self, ctx:TypeScriptParser.UnaryPlusExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#UnaryPlusExpression.
    def exitUnaryPlusExpression(self, ctx:TypeScriptParser.UnaryPlusExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#DeleteExpression.
    def enterDeleteExpression(self, ctx:TypeScriptParser.DeleteExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#DeleteExpression.
    def exitDeleteExpression(self, ctx:TypeScriptParser.DeleteExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#GeneratorsFunctionExpression.
    def enterGeneratorsFunctionExpression(self, ctx:TypeScriptParser.GeneratorsFunctionExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#GeneratorsFunctionExpression.
    def exitGeneratorsFunctionExpression(self, ctx:TypeScriptParser.GeneratorsFunctionExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ArrowFunctionExpression.
    def enterArrowFunctionExpression(self, ctx:TypeScriptParser.ArrowFunctionExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ArrowFunctionExpression.
    def exitArrowFunctionExpression(self, ctx:TypeScriptParser.ArrowFunctionExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#IteratorsExpression.
    def enterIteratorsExpression(self, ctx:TypeScriptParser.IteratorsExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#IteratorsExpression.
    def exitIteratorsExpression(self, ctx:TypeScriptParser.IteratorsExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#EqualityExpression.
    def enterEqualityExpression(self, ctx:TypeScriptParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#EqualityExpression.
    def exitEqualityExpression(self, ctx:TypeScriptParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#BitXOrExpression.
    def enterBitXOrExpression(self, ctx:TypeScriptParser.BitXOrExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#BitXOrExpression.
    def exitBitXOrExpression(self, ctx:TypeScriptParser.BitXOrExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#CastAsExpression.
    def enterCastAsExpression(self, ctx:TypeScriptParser.CastAsExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#CastAsExpression.
    def exitCastAsExpression(self, ctx:TypeScriptParser.CastAsExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#SuperExpression.
    def enterSuperExpression(self, ctx:TypeScriptParser.SuperExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#SuperExpression.
    def exitSuperExpression(self, ctx:TypeScriptParser.SuperExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:TypeScriptParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:TypeScriptParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#BitShiftExpression.
    def enterBitShiftExpression(self, ctx:TypeScriptParser.BitShiftExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#BitShiftExpression.
    def exitBitShiftExpression(self, ctx:TypeScriptParser.BitShiftExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:TypeScriptParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:TypeScriptParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx:TypeScriptParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx:TypeScriptParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#RelationalExpression.
    def enterRelationalExpression(self, ctx:TypeScriptParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#RelationalExpression.
    def exitRelationalExpression(self, ctx:TypeScriptParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#PostIncrementExpression.
    def enterPostIncrementExpression(self, ctx:TypeScriptParser.PostIncrementExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#PostIncrementExpression.
    def exitPostIncrementExpression(self, ctx:TypeScriptParser.PostIncrementExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#YieldExpression.
    def enterYieldExpression(self, ctx:TypeScriptParser.YieldExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#YieldExpression.
    def exitYieldExpression(self, ctx:TypeScriptParser.YieldExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#BitNotExpression.
    def enterBitNotExpression(self, ctx:TypeScriptParser.BitNotExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#BitNotExpression.
    def exitBitNotExpression(self, ctx:TypeScriptParser.BitNotExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#NewExpression.
    def enterNewExpression(self, ctx:TypeScriptParser.NewExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#NewExpression.
    def exitNewExpression(self, ctx:TypeScriptParser.NewExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#LiteralExpression.
    def enterLiteralExpression(self, ctx:TypeScriptParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#LiteralExpression.
    def exitLiteralExpression(self, ctx:TypeScriptParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ArrayLiteralExpression.
    def enterArrayLiteralExpression(self, ctx:TypeScriptParser.ArrayLiteralExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ArrayLiteralExpression.
    def exitArrayLiteralExpression(self, ctx:TypeScriptParser.ArrayLiteralExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#MemberDotExpression.
    def enterMemberDotExpression(self, ctx:TypeScriptParser.MemberDotExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#MemberDotExpression.
    def exitMemberDotExpression(self, ctx:TypeScriptParser.MemberDotExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#ClassExpression.
    def enterClassExpression(self, ctx:TypeScriptParser.ClassExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#ClassExpression.
    def exitClassExpression(self, ctx:TypeScriptParser.ClassExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#MemberIndexExpression.
    def enterMemberIndexExpression(self, ctx:TypeScriptParser.MemberIndexExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#MemberIndexExpression.
    def exitMemberIndexExpression(self, ctx:TypeScriptParser.MemberIndexExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#IdentifierExpression.
    def enterIdentifierExpression(self, ctx:TypeScriptParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#IdentifierExpression.
    def exitIdentifierExpression(self, ctx:TypeScriptParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#BitAndExpression.
    def enterBitAndExpression(self, ctx:TypeScriptParser.BitAndExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#BitAndExpression.
    def exitBitAndExpression(self, ctx:TypeScriptParser.BitAndExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#BitOrExpression.
    def enterBitOrExpression(self, ctx:TypeScriptParser.BitOrExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#BitOrExpression.
    def exitBitOrExpression(self, ctx:TypeScriptParser.BitOrExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#AssignmentOperatorExpression.
    def enterAssignmentOperatorExpression(self, ctx:TypeScriptParser.AssignmentOperatorExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#AssignmentOperatorExpression.
    def exitAssignmentOperatorExpression(self, ctx:TypeScriptParser.AssignmentOperatorExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#VoidExpression.
    def enterVoidExpression(self, ctx:TypeScriptParser.VoidExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#VoidExpression.
    def exitVoidExpression(self, ctx:TypeScriptParser.VoidExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#asExpression.
    def enterAsExpression(self, ctx:TypeScriptParser.AsExpressionContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#asExpression.
    def exitAsExpression(self, ctx:TypeScriptParser.AsExpressionContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#arrowFunctionDeclaration.
    def enterArrowFunctionDeclaration(self, ctx:TypeScriptParser.ArrowFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#arrowFunctionDeclaration.
    def exitArrowFunctionDeclaration(self, ctx:TypeScriptParser.ArrowFunctionDeclarationContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#arrowFunctionParameters.
    def enterArrowFunctionParameters(self, ctx:TypeScriptParser.ArrowFunctionParametersContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#arrowFunctionParameters.
    def exitArrowFunctionParameters(self, ctx:TypeScriptParser.ArrowFunctionParametersContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#arrowFunctionBody.
    def enterArrowFunctionBody(self, ctx:TypeScriptParser.ArrowFunctionBodyContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#arrowFunctionBody.
    def exitArrowFunctionBody(self, ctx:TypeScriptParser.ArrowFunctionBodyContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:TypeScriptParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:TypeScriptParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#literal.
    def enterLiteral(self, ctx:TypeScriptParser.LiteralContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#literal.
    def exitLiteral(self, ctx:TypeScriptParser.LiteralContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#templateStringLiteral.
    def enterTemplateStringLiteral(self, ctx:TypeScriptParser.TemplateStringLiteralContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#templateStringLiteral.
    def exitTemplateStringLiteral(self, ctx:TypeScriptParser.TemplateStringLiteralContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#templateStringAtom.
    def enterTemplateStringAtom(self, ctx:TypeScriptParser.TemplateStringAtomContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#templateStringAtom.
    def exitTemplateStringAtom(self, ctx:TypeScriptParser.TemplateStringAtomContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#numericLiteral.
    def enterNumericLiteral(self, ctx:TypeScriptParser.NumericLiteralContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#numericLiteral.
    def exitNumericLiteral(self, ctx:TypeScriptParser.NumericLiteralContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#identifierName.
    def enterIdentifierName(self, ctx:TypeScriptParser.IdentifierNameContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#identifierName.
    def exitIdentifierName(self, ctx:TypeScriptParser.IdentifierNameContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#identifierOrKeyWord.
    def enterIdentifierOrKeyWord(self, ctx:TypeScriptParser.IdentifierOrKeyWordContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#identifierOrKeyWord.
    def exitIdentifierOrKeyWord(self, ctx:TypeScriptParser.IdentifierOrKeyWordContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#reservedWord.
    def enterReservedWord(self, ctx:TypeScriptParser.ReservedWordContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#reservedWord.
    def exitReservedWord(self, ctx:TypeScriptParser.ReservedWordContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#keyword.
    def enterKeyword(self, ctx:TypeScriptParser.KeywordContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#keyword.
    def exitKeyword(self, ctx:TypeScriptParser.KeywordContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#getter.
    def enterGetter(self, ctx:TypeScriptParser.GetterContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#getter.
    def exitGetter(self, ctx:TypeScriptParser.GetterContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#setter.
    def enterSetter(self, ctx:TypeScriptParser.SetterContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#setter.
    def exitSetter(self, ctx:TypeScriptParser.SetterContext):
        pass


    # Enter a parse tree produced by TypeScriptParser#eos.
    def enterEos(self, ctx:TypeScriptParser.EosContext):
        pass

    # Exit a parse tree produced by TypeScriptParser#eos.
    def exitEos(self, ctx:TypeScriptParser.EosContext):
        pass



del TypeScriptParser