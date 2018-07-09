def setup():
    size(800, 800) # Set the window size
    background(0, 200, 255) #Set background color
    r= 255
    textSize(85)
    fill(r,0,r)
    text("Rae-Vin's Sunshine", 10, 100)
    noStroke() #Start of grass
    fill(0,r,0)
    rect(0 ,600,800,600) #End of grass
    noStroke()
    fill(r,r,0) 
    ellipse (400, 400, 250, 250)
    p= random (80, 200)
    fill(r,r,r) # Cloud 1
    ellipse(p  ,170, 90,50)
    fill(r,r,r) 
    ellipse(p +50, 145, 90, 50)
    
    noStroke() 
    fill(r,r,r) # Cloud 2
    ellipse(p + 400,175, 90, 50)
    fill(r,r,r) 
    ellipse(p + 450, 155, 90, 50)
    
    fill(r,r,r) # Cloud 3
    ellipse(p +250  ,250, 90,50)
    fill(r,r,r) 
    ellipse(p +200  ,220, 90,50)
    
    stroke(r,r,0)
    line(200,400,300,400) #Rays 1
    
