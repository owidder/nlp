# Generated from typeScript/TypeScriptParser.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TypeScriptParser import TypeScriptParser
else:
    from TypeScriptParser import TypeScriptParser

# This class defines a complete generic visitor for a parse tree produced by TypeScriptParser.

class TypeScriptParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TypeScriptParser#initializer.
    def visitInitializer(self, ctx:TypeScriptParser.InitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#bindingPattern.
    def visitBindingPattern(self, ctx:TypeScriptParser.BindingPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeParameters.
    def visitTypeParameters(self, ctx:TypeScriptParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeParameterList.
    def visitTypeParameterList(self, ctx:TypeScriptParser.TypeParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeParameter.
    def visitTypeParameter(self, ctx:TypeScriptParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#constraint.
    def visitConstraint(self, ctx:TypeScriptParser.ConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeArguments.
    def visitTypeArguments(self, ctx:TypeScriptParser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeArgumentList.
    def visitTypeArgumentList(self, ctx:TypeScriptParser.TypeArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeArgument.
    def visitTypeArgument(self, ctx:TypeScriptParser.TypeArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#type_.
    def visitType_(self, ctx:TypeScriptParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#Intersection.
    def visitIntersection(self, ctx:TypeScriptParser.IntersectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#Primary.
    def visitPrimary(self, ctx:TypeScriptParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#Union.
    def visitUnion(self, ctx:TypeScriptParser.UnionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#RedefinitionOfType.
    def visitRedefinitionOfType(self, ctx:TypeScriptParser.RedefinitionOfTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#PredefinedPrimType.
    def visitPredefinedPrimType(self, ctx:TypeScriptParser.PredefinedPrimTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ArrayPrimType.
    def visitArrayPrimType(self, ctx:TypeScriptParser.ArrayPrimTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ParenthesizedPrimType.
    def visitParenthesizedPrimType(self, ctx:TypeScriptParser.ParenthesizedPrimTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ThisPrimType.
    def visitThisPrimType(self, ctx:TypeScriptParser.ThisPrimTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#TuplePrimType.
    def visitTuplePrimType(self, ctx:TypeScriptParser.TuplePrimTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ObjectPrimType.
    def visitObjectPrimType(self, ctx:TypeScriptParser.ObjectPrimTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ReferencePrimType.
    def visitReferencePrimType(self, ctx:TypeScriptParser.ReferencePrimTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#QueryPrimType.
    def visitQueryPrimType(self, ctx:TypeScriptParser.QueryPrimTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#predefinedType.
    def visitPredefinedType(self, ctx:TypeScriptParser.PredefinedTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeReference.
    def visitTypeReference(self, ctx:TypeScriptParser.TypeReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#nestedTypeGeneric.
    def visitNestedTypeGeneric(self, ctx:TypeScriptParser.NestedTypeGenericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeGeneric.
    def visitTypeGeneric(self, ctx:TypeScriptParser.TypeGenericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeIncludeGeneric.
    def visitTypeIncludeGeneric(self, ctx:TypeScriptParser.TypeIncludeGenericContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeName.
    def visitTypeName(self, ctx:TypeScriptParser.TypeNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#objectType.
    def visitObjectType(self, ctx:TypeScriptParser.ObjectTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeBody.
    def visitTypeBody(self, ctx:TypeScriptParser.TypeBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeMemberList.
    def visitTypeMemberList(self, ctx:TypeScriptParser.TypeMemberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeMember.
    def visitTypeMember(self, ctx:TypeScriptParser.TypeMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#arrayType.
    def visitArrayType(self, ctx:TypeScriptParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#tupleType.
    def visitTupleType(self, ctx:TypeScriptParser.TupleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#tupleElementTypes.
    def visitTupleElementTypes(self, ctx:TypeScriptParser.TupleElementTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#functionType.
    def visitFunctionType(self, ctx:TypeScriptParser.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#constructorType.
    def visitConstructorType(self, ctx:TypeScriptParser.ConstructorTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeQuery.
    def visitTypeQuery(self, ctx:TypeScriptParser.TypeQueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeQueryExpression.
    def visitTypeQueryExpression(self, ctx:TypeScriptParser.TypeQueryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#propertySignatur.
    def visitPropertySignatur(self, ctx:TypeScriptParser.PropertySignaturContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeAnnotation.
    def visitTypeAnnotation(self, ctx:TypeScriptParser.TypeAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#callSignature.
    def visitCallSignature(self, ctx:TypeScriptParser.CallSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#parameterList.
    def visitParameterList(self, ctx:TypeScriptParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#requiredParameterList.
    def visitRequiredParameterList(self, ctx:TypeScriptParser.RequiredParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#parameter.
    def visitParameter(self, ctx:TypeScriptParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#optionalParameter.
    def visitOptionalParameter(self, ctx:TypeScriptParser.OptionalParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#restParameter.
    def visitRestParameter(self, ctx:TypeScriptParser.RestParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#requiredParameter.
    def visitRequiredParameter(self, ctx:TypeScriptParser.RequiredParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#accessibilityModifier.
    def visitAccessibilityModifier(self, ctx:TypeScriptParser.AccessibilityModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#identifierOrPattern.
    def visitIdentifierOrPattern(self, ctx:TypeScriptParser.IdentifierOrPatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#constructSignature.
    def visitConstructSignature(self, ctx:TypeScriptParser.ConstructSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#indexSignature.
    def visitIndexSignature(self, ctx:TypeScriptParser.IndexSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#methodSignature.
    def visitMethodSignature(self, ctx:TypeScriptParser.MethodSignatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#typeAliasDeclaration.
    def visitTypeAliasDeclaration(self, ctx:TypeScriptParser.TypeAliasDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:TypeScriptParser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#interfaceDeclaration.
    def visitInterfaceDeclaration(self, ctx:TypeScriptParser.InterfaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#interfaceExtendsClause.
    def visitInterfaceExtendsClause(self, ctx:TypeScriptParser.InterfaceExtendsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#classOrInterfaceTypeList.
    def visitClassOrInterfaceTypeList(self, ctx:TypeScriptParser.ClassOrInterfaceTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#enumDeclaration.
    def visitEnumDeclaration(self, ctx:TypeScriptParser.EnumDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#enumBody.
    def visitEnumBody(self, ctx:TypeScriptParser.EnumBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#enumMemberList.
    def visitEnumMemberList(self, ctx:TypeScriptParser.EnumMemberListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#enumMember.
    def visitEnumMember(self, ctx:TypeScriptParser.EnumMemberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#namespaceDeclaration.
    def visitNamespaceDeclaration(self, ctx:TypeScriptParser.NamespaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#namespaceName.
    def visitNamespaceName(self, ctx:TypeScriptParser.NamespaceNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#importAliasDeclaration.
    def visitImportAliasDeclaration(self, ctx:TypeScriptParser.ImportAliasDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#decoratorList.
    def visitDecoratorList(self, ctx:TypeScriptParser.DecoratorListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#decorator.
    def visitDecorator(self, ctx:TypeScriptParser.DecoratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#decoratorMemberExpression.
    def visitDecoratorMemberExpression(self, ctx:TypeScriptParser.DecoratorMemberExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#decoratorCallExpression.
    def visitDecoratorCallExpression(self, ctx:TypeScriptParser.DecoratorCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#program.
    def visitProgram(self, ctx:TypeScriptParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#sourceElement.
    def visitSourceElement(self, ctx:TypeScriptParser.SourceElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#statement.
    def visitStatement(self, ctx:TypeScriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#block.
    def visitBlock(self, ctx:TypeScriptParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#statementList.
    def visitStatementList(self, ctx:TypeScriptParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#abstractDeclaration.
    def visitAbstractDeclaration(self, ctx:TypeScriptParser.AbstractDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#importStatement.
    def visitImportStatement(self, ctx:TypeScriptParser.ImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#fromBlock.
    def visitFromBlock(self, ctx:TypeScriptParser.FromBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#multipleImportStatement.
    def visitMultipleImportStatement(self, ctx:TypeScriptParser.MultipleImportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#exportStatement.
    def visitExportStatement(self, ctx:TypeScriptParser.ExportStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#variableStatement.
    def visitVariableStatement(self, ctx:TypeScriptParser.VariableStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#variableDeclarationList.
    def visitVariableDeclarationList(self, ctx:TypeScriptParser.VariableDeclarationListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:TypeScriptParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#emptyStatement.
    def visitEmptyStatement(self, ctx:TypeScriptParser.EmptyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#expressionStatement.
    def visitExpressionStatement(self, ctx:TypeScriptParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ifStatement.
    def visitIfStatement(self, ctx:TypeScriptParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#DoStatement.
    def visitDoStatement(self, ctx:TypeScriptParser.DoStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#WhileStatement.
    def visitWhileStatement(self, ctx:TypeScriptParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ForStatement.
    def visitForStatement(self, ctx:TypeScriptParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ForVarStatement.
    def visitForVarStatement(self, ctx:TypeScriptParser.ForVarStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ForInStatement.
    def visitForInStatement(self, ctx:TypeScriptParser.ForInStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ForVarInStatement.
    def visitForVarInStatement(self, ctx:TypeScriptParser.ForVarInStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#varModifier.
    def visitVarModifier(self, ctx:TypeScriptParser.VarModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#continueStatement.
    def visitContinueStatement(self, ctx:TypeScriptParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#breakStatement.
    def visitBreakStatement(self, ctx:TypeScriptParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#returnStatement.
    def visitReturnStatement(self, ctx:TypeScriptParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#yieldStatement.
    def visitYieldStatement(self, ctx:TypeScriptParser.YieldStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#withStatement.
    def visitWithStatement(self, ctx:TypeScriptParser.WithStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#switchStatement.
    def visitSwitchStatement(self, ctx:TypeScriptParser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#caseBlock.
    def visitCaseBlock(self, ctx:TypeScriptParser.CaseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#caseClauses.
    def visitCaseClauses(self, ctx:TypeScriptParser.CaseClausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#caseClause.
    def visitCaseClause(self, ctx:TypeScriptParser.CaseClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#defaultClause.
    def visitDefaultClause(self, ctx:TypeScriptParser.DefaultClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#labelledStatement.
    def visitLabelledStatement(self, ctx:TypeScriptParser.LabelledStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#throwStatement.
    def visitThrowStatement(self, ctx:TypeScriptParser.ThrowStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#tryStatement.
    def visitTryStatement(self, ctx:TypeScriptParser.TryStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#catchProduction.
    def visitCatchProduction(self, ctx:TypeScriptParser.CatchProductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#finallyProduction.
    def visitFinallyProduction(self, ctx:TypeScriptParser.FinallyProductionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#debuggerStatement.
    def visitDebuggerStatement(self, ctx:TypeScriptParser.DebuggerStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:TypeScriptParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#classDeclaration.
    def visitClassDeclaration(self, ctx:TypeScriptParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#classHeritage.
    def visitClassHeritage(self, ctx:TypeScriptParser.ClassHeritageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#classTail.
    def visitClassTail(self, ctx:TypeScriptParser.ClassTailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#classExtendsClause.
    def visitClassExtendsClause(self, ctx:TypeScriptParser.ClassExtendsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#implementsClause.
    def visitImplementsClause(self, ctx:TypeScriptParser.ImplementsClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#classElement.
    def visitClassElement(self, ctx:TypeScriptParser.ClassElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#PropertyDeclarationExpression.
    def visitPropertyDeclarationExpression(self, ctx:TypeScriptParser.PropertyDeclarationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#MethodDeclarationExpression.
    def visitMethodDeclarationExpression(self, ctx:TypeScriptParser.MethodDeclarationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#GetterSetterDeclarationExpression.
    def visitGetterSetterDeclarationExpression(self, ctx:TypeScriptParser.GetterSetterDeclarationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#AbstractMemberDeclaration.
    def visitAbstractMemberDeclaration(self, ctx:TypeScriptParser.AbstractMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#propertyMemberBase.
    def visitPropertyMemberBase(self, ctx:TypeScriptParser.PropertyMemberBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#indexMemberDeclaration.
    def visitIndexMemberDeclaration(self, ctx:TypeScriptParser.IndexMemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#generatorMethod.
    def visitGeneratorMethod(self, ctx:TypeScriptParser.GeneratorMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#generatorFunctionDeclaration.
    def visitGeneratorFunctionDeclaration(self, ctx:TypeScriptParser.GeneratorFunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#generatorBlock.
    def visitGeneratorBlock(self, ctx:TypeScriptParser.GeneratorBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#generatorDefinition.
    def visitGeneratorDefinition(self, ctx:TypeScriptParser.GeneratorDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#iteratorBlock.
    def visitIteratorBlock(self, ctx:TypeScriptParser.IteratorBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#iteratorDefinition.
    def visitIteratorDefinition(self, ctx:TypeScriptParser.IteratorDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#formalParameterList.
    def visitFormalParameterList(self, ctx:TypeScriptParser.FormalParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#formalParameterArg.
    def visitFormalParameterArg(self, ctx:TypeScriptParser.FormalParameterArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#lastFormalParameterArg.
    def visitLastFormalParameterArg(self, ctx:TypeScriptParser.LastFormalParameterArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#functionBody.
    def visitFunctionBody(self, ctx:TypeScriptParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#sourceElements.
    def visitSourceElements(self, ctx:TypeScriptParser.SourceElementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#arrayLiteral.
    def visitArrayLiteral(self, ctx:TypeScriptParser.ArrayLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#elementList.
    def visitElementList(self, ctx:TypeScriptParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#arrayElement.
    def visitArrayElement(self, ctx:TypeScriptParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#objectLiteral.
    def visitObjectLiteral(self, ctx:TypeScriptParser.ObjectLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#PropertyExpressionAssignment.
    def visitPropertyExpressionAssignment(self, ctx:TypeScriptParser.PropertyExpressionAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ComputedPropertyExpressionAssignment.
    def visitComputedPropertyExpressionAssignment(self, ctx:TypeScriptParser.ComputedPropertyExpressionAssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#PropertyGetter.
    def visitPropertyGetter(self, ctx:TypeScriptParser.PropertyGetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#PropertySetter.
    def visitPropertySetter(self, ctx:TypeScriptParser.PropertySetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#MethodProperty.
    def visitMethodProperty(self, ctx:TypeScriptParser.MethodPropertyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#PropertyShorthand.
    def visitPropertyShorthand(self, ctx:TypeScriptParser.PropertyShorthandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#RestParameterInObject.
    def visitRestParameterInObject(self, ctx:TypeScriptParser.RestParameterInObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#getAccessor.
    def visitGetAccessor(self, ctx:TypeScriptParser.GetAccessorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#setAccessor.
    def visitSetAccessor(self, ctx:TypeScriptParser.SetAccessorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#propertyName.
    def visitPropertyName(self, ctx:TypeScriptParser.PropertyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#arguments.
    def visitArguments(self, ctx:TypeScriptParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#argumentList.
    def visitArgumentList(self, ctx:TypeScriptParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#argument.
    def visitArgument(self, ctx:TypeScriptParser.ArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#expressionSequence.
    def visitExpressionSequence(self, ctx:TypeScriptParser.ExpressionSequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#functionExpressionDeclaration.
    def visitFunctionExpressionDeclaration(self, ctx:TypeScriptParser.FunctionExpressionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#TemplateStringExpression.
    def visitTemplateStringExpression(self, ctx:TypeScriptParser.TemplateStringExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#TernaryExpression.
    def visitTernaryExpression(self, ctx:TypeScriptParser.TernaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#LogicalAndExpression.
    def visitLogicalAndExpression(self, ctx:TypeScriptParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#GeneratorsExpression.
    def visitGeneratorsExpression(self, ctx:TypeScriptParser.GeneratorsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#PreIncrementExpression.
    def visitPreIncrementExpression(self, ctx:TypeScriptParser.PreIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ObjectLiteralExpression.
    def visitObjectLiteralExpression(self, ctx:TypeScriptParser.ObjectLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#InExpression.
    def visitInExpression(self, ctx:TypeScriptParser.InExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#LogicalOrExpression.
    def visitLogicalOrExpression(self, ctx:TypeScriptParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#GenericTypes.
    def visitGenericTypes(self, ctx:TypeScriptParser.GenericTypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#NotExpression.
    def visitNotExpression(self, ctx:TypeScriptParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#PreDecreaseExpression.
    def visitPreDecreaseExpression(self, ctx:TypeScriptParser.PreDecreaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ArgumentsExpression.
    def visitArgumentsExpression(self, ctx:TypeScriptParser.ArgumentsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ThisExpression.
    def visitThisExpression(self, ctx:TypeScriptParser.ThisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#FunctionExpression.
    def visitFunctionExpression(self, ctx:TypeScriptParser.FunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#UnaryMinusExpression.
    def visitUnaryMinusExpression(self, ctx:TypeScriptParser.UnaryMinusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#AssignmentExpression.
    def visitAssignmentExpression(self, ctx:TypeScriptParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#PostDecreaseExpression.
    def visitPostDecreaseExpression(self, ctx:TypeScriptParser.PostDecreaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#TypeofExpression.
    def visitTypeofExpression(self, ctx:TypeScriptParser.TypeofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#InstanceofExpression.
    def visitInstanceofExpression(self, ctx:TypeScriptParser.InstanceofExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#UnaryPlusExpression.
    def visitUnaryPlusExpression(self, ctx:TypeScriptParser.UnaryPlusExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#DeleteExpression.
    def visitDeleteExpression(self, ctx:TypeScriptParser.DeleteExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#GeneratorsFunctionExpression.
    def visitGeneratorsFunctionExpression(self, ctx:TypeScriptParser.GeneratorsFunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ArrowFunctionExpression.
    def visitArrowFunctionExpression(self, ctx:TypeScriptParser.ArrowFunctionExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#IteratorsExpression.
    def visitIteratorsExpression(self, ctx:TypeScriptParser.IteratorsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#EqualityExpression.
    def visitEqualityExpression(self, ctx:TypeScriptParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#BitXOrExpression.
    def visitBitXOrExpression(self, ctx:TypeScriptParser.BitXOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#CastAsExpression.
    def visitCastAsExpression(self, ctx:TypeScriptParser.CastAsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#SuperExpression.
    def visitSuperExpression(self, ctx:TypeScriptParser.SuperExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#MultiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:TypeScriptParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#BitShiftExpression.
    def visitBitShiftExpression(self, ctx:TypeScriptParser.BitShiftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ParenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:TypeScriptParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#AdditiveExpression.
    def visitAdditiveExpression(self, ctx:TypeScriptParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#RelationalExpression.
    def visitRelationalExpression(self, ctx:TypeScriptParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#PostIncrementExpression.
    def visitPostIncrementExpression(self, ctx:TypeScriptParser.PostIncrementExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#YieldExpression.
    def visitYieldExpression(self, ctx:TypeScriptParser.YieldExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#BitNotExpression.
    def visitBitNotExpression(self, ctx:TypeScriptParser.BitNotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#NewExpression.
    def visitNewExpression(self, ctx:TypeScriptParser.NewExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#LiteralExpression.
    def visitLiteralExpression(self, ctx:TypeScriptParser.LiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ArrayLiteralExpression.
    def visitArrayLiteralExpression(self, ctx:TypeScriptParser.ArrayLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#MemberDotExpression.
    def visitMemberDotExpression(self, ctx:TypeScriptParser.MemberDotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#ClassExpression.
    def visitClassExpression(self, ctx:TypeScriptParser.ClassExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#MemberIndexExpression.
    def visitMemberIndexExpression(self, ctx:TypeScriptParser.MemberIndexExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#IdentifierExpression.
    def visitIdentifierExpression(self, ctx:TypeScriptParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#BitAndExpression.
    def visitBitAndExpression(self, ctx:TypeScriptParser.BitAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#BitOrExpression.
    def visitBitOrExpression(self, ctx:TypeScriptParser.BitOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#AssignmentOperatorExpression.
    def visitAssignmentOperatorExpression(self, ctx:TypeScriptParser.AssignmentOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#VoidExpression.
    def visitVoidExpression(self, ctx:TypeScriptParser.VoidExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#asExpression.
    def visitAsExpression(self, ctx:TypeScriptParser.AsExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#arrowFunctionDeclaration.
    def visitArrowFunctionDeclaration(self, ctx:TypeScriptParser.ArrowFunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#arrowFunctionParameters.
    def visitArrowFunctionParameters(self, ctx:TypeScriptParser.ArrowFunctionParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#arrowFunctionBody.
    def visitArrowFunctionBody(self, ctx:TypeScriptParser.ArrowFunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:TypeScriptParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#literal.
    def visitLiteral(self, ctx:TypeScriptParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#templateStringLiteral.
    def visitTemplateStringLiteral(self, ctx:TypeScriptParser.TemplateStringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#templateStringAtom.
    def visitTemplateStringAtom(self, ctx:TypeScriptParser.TemplateStringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#numericLiteral.
    def visitNumericLiteral(self, ctx:TypeScriptParser.NumericLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#identifierName.
    def visitIdentifierName(self, ctx:TypeScriptParser.IdentifierNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#identifierOrKeyWord.
    def visitIdentifierOrKeyWord(self, ctx:TypeScriptParser.IdentifierOrKeyWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#reservedWord.
    def visitReservedWord(self, ctx:TypeScriptParser.ReservedWordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#keyword.
    def visitKeyword(self, ctx:TypeScriptParser.KeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#getter.
    def visitGetter(self, ctx:TypeScriptParser.GetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#setter.
    def visitSetter(self, ctx:TypeScriptParser.SetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TypeScriptParser#eos.
    def visitEos(self, ctx:TypeScriptParser.EosContext):
        return self.visitChildren(ctx)



del TypeScriptParser