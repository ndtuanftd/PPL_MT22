class CodeGeneration:
    
    # vardecl -> return Symbol(name, typ, value)
    def visitVarDecl(self,ctx,o):
        if o.frame is None: # global
            code = self.emit.emitATTRIBUTE(ctx.name, ctx.typ, False)
            self.emit.printout(code)
            return Symbol(ctx.name, ctx.typ, CName(self.className))
        else: # local
            index  = o.frame.getNewIndex()  # get new index from frame
            code = self.emit.emitVAR(index, ctx.name, ctx.typ, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
            self.emit.printout(code)
            return Symbol(ctx.name, ctx.typ, Index(index))

            
            
    
    # visit lit -> tra ve 2 thứ (1: code tương đương của expr, 2: kiểu của expr)
    def visitIntLiteral(self,ctx,o):  
        # value of int literal is in ctx.value
        # frame = o.frame
        code = self.emit.emitPUSHICONST(ctx.value, o.frame)  # nhờ Emitter để tạo code cho mình
        typ = IntType()
        
        return code, typ
    
    # visit BinOp -> return code gen (e1c + e2c + op) + return type
    def vistBinOp(self,ctx,o):
        """ 
        BinOP: 
            e1: Expr, 
            e2: Expr,
            op: str, // +-*/
            
        """
        e1c, e1t = self.visit(ctx.e1, o)   # traverse to e1 to get code + type
        e2c, r2t = self.visit(ctx.e2, o)  # traverse to e2 to get code + type
        
        # type preprocessing
        if type(e1t) is type(e2t):
            rettype = e1t
        elif type(e1t) is IntType and type(e2t) is FloatType:
            e1c = e1c + self.emit.emitI2F(o.frame) # convert e1 type from int to float
            rettype = e2t # return type is float
        else: # e2 is int and e1 is float
            e2c = e2c + self.emit.emitI2F(o.frame) # convert e2 type from int to float
            rettype = e1t # return type is float
            
        if ctx.op in ['+', '-']:
            op = self.emit.emitADDOP(ctx.op, rettype, o.frame)
        elif ctx.op in ['*']:
            op = self.emit.emitMULOP(ctx.op, rettype, o.frame)
        elif ctx.op in ['/']:
            if type(e1t) is IntType and type(e2t) is IntType:
                e1c = e1c + self.emit.emitI2F(o.frame) # convert e1 type from int to float
                e2c = e2c + self.emit.emitI2F(o.frame) # convert e2 type from int to float
        else: # compare op
            op = self.emit.emitREOP(ctx.op, rettype, o.frame)   # 
            rettype = BoolType()
        
        return e1c + e2c + op, rettype
    
    #  visit Id -> return code gen (READVAR or GETSTATIC) + return type
    def visitId(self, ctx,o):
        sym = list(filter(lambda x: x.name == ctx.name, o.sym))[0] # lọc symbol dau tien co ten la name
        if o.isLeft: # is left -> LHS -> emitWRITEVAR()
            if type(sym.value) is Index:
                code = self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame)
            else:
                code = self.emit.emitPUTSTATIC(sym.value.value + '.' + sym.name, sym.mtype, o.frame)
        else: # is right -> RHS -> emitREADVAR()
            if type(sym.value) is Index:  # is index -> local variable -> emitREADVAR()
                code = self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame)
            else: # is CNAME -> global variable -> emitGETSTATIC() (accessed by format class_name.method => value.name)
                code = self.emit.emitGETSTATIC(sym.value.value + '.' + sym.name, sym.mtype, o.frame)   
        return code, sym.mtype
    
    
    def visitAssignStmt(self, ctx, o):
        rc, rt = self.visit(ctx.rhs, Access(o.frame, o.sym, False))
        self.emit.printout(rc)
        
        lc, lt = self.visit(ctx.lhs, Access(o.frame, o.sym, True))
        self.emit.printout(lc)
        
        
    def visitIf(self, ctx, o):
        # code gen for expr
        ec, et = self.visit(ctx.expr, Access(o.frame, o.sym, False))
        self.emit.printout(ec)
        
        # get fLabel from frame
        fLabel = o.frame.getNewLabel()
        
        # Jump to fLabel if expr is false
        code = self.emit.emitIFFALSE(fLabel, o.frame)
        self.emit.printout(code)
        
        # code gen for tstmt
        self.visit(ctx.tstmt, o)
        
        if ctx.fstmt is None:
            # Put fLabel here
            code = self.emit.emitLABEL(fLabel, o.frame)
            self.emit.printout(code)
        else:
            # get eLabel from frame
            eLabel = o.frame.getNewLabel()
            # jump to tLabel
            code = self.emit.emitLabel(eLabel, o.frame)
            
            # put fLabel here
            code = self.emit.emitLABEL(fLabel, o.frame)
            self.emit.printout(code)
            
            # gen code for estmt
            self.visit(ctx.fstmt, o)
            
            # put eLabel here
            code = self.emit.emitLABEL(eLabel, o.frame)