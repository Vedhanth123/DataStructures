def point(px, py, qx, qy):
    yx = yy = 0
    slopex = float(qy - py)
    
    slopey = float(qx - px)
    
    
    def algebra(var,const,ans):
        
        # x - x1 = slope

        return  const + ans
    yx = algebra(yx,qx,slopex)
    yy = algebra(yy,qy,slopey)

    return (int(yx),int(yy))


print(point(7,8,9,1))