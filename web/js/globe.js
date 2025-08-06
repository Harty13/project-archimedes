/**
 * 3D Globe Visualization for The Great Game
 * Uses Three.js to create an interactive rotating globe
 */

class Globe {
    constructor(canvasId) {
        this.canvas = document.getElementById(canvasId);
        this.scene = null;
        this.camera = null;
        this.renderer = null;
        this.globe = null;
        this.atmosphere = null;
        this.stars = null;
        this.animationId = null;
        
        // Globe state
        this.rotationSpeed = 0.005;
        this.isRotating = true;
        this.currentProbability = 0.5;
        
        this.init();
    }

    init() {
        this.createScene();
        this.createCamera();
        this.createRenderer();
        this.createLights();
        this.createStars();
        this.createGlobe();
        this.createAtmosphere();
        this.addEventListeners();
        this.animate();
    }

    createScene() {
        this.scene = new THREE.Scene();
        this.scene.background = new THREE.Color(0x000011);
    }

    createCamera() {
        const aspect = this.canvas.clientWidth / this.canvas.clientHeight;
        this.camera = new THREE.PerspectiveCamera(75, aspect, 0.1, 1000);
        this.camera.position.set(-1, 0, 3); // Shift camera to the right (negative X moves camera right, making globe appear on the right)
    }

    createRenderer() {
        this.renderer = new THREE.WebGLRenderer({
            canvas: this.canvas,
            antialias: true,
            alpha: true
        });
        this.renderer.setSize(this.canvas.clientWidth, this.canvas.clientHeight);
        this.renderer.setPixelRatio(window.devicePixelRatio);
        this.renderer.shadowMap.enabled = true;
        this.renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    }

    createLights() {
        // Ambient light
        const ambientLight = new THREE.AmbientLight(0x404040, 0.4);
        this.scene.add(ambientLight);

        // Directional light (sun)
        const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
        directionalLight.position.set(5, 3, 5);
        directionalLight.castShadow = true;
        directionalLight.shadow.mapSize.width = 2048;
        directionalLight.shadow.mapSize.height = 2048;
        this.scene.add(directionalLight);

        // Point light for atmosphere glow
        const pointLight = new THREE.PointLight(0x4488ff, 0.5, 10);
        pointLight.position.set(0, 0, 2);
        this.scene.add(pointLight);
    }

    createStars() {
        const starsGeometry = new THREE.BufferGeometry();
        const starsCount = 2000;
        const positions = new Float32Array(starsCount * 3);

        for (let i = 0; i < starsCount * 3; i++) {
            positions[i] = (Math.random() - 0.5) * 100;
        }

        starsGeometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

        const starsMaterial = new THREE.PointsMaterial({
            color: 0xffffff,
            size: 0.5,
            transparent: true,
            opacity: 0.8
        });

        this.stars = new THREE.Points(starsGeometry, starsMaterial);
        this.scene.add(this.stars);
    }

    createGlobe() {
        const geometry = new THREE.SphereGeometry(1, 64, 64);
        
        // Create earth-like texture
        const canvas = document.createElement('canvas');
        canvas.width = 1024;
        canvas.height = 512;
        const ctx = canvas.getContext('2d');
        
        // Create a gradient that looks like continents
        this.drawEarthTexture(ctx, canvas.width, canvas.height);
        
        const texture = new THREE.CanvasTexture(canvas);
        texture.wrapS = THREE.RepeatWrapping;
        texture.wrapT = THREE.RepeatWrapping;

        const material = new THREE.MeshPhongMaterial({
            map: texture,
            transparent: true,
            opacity: 0.9
        });

        this.globe = new THREE.Mesh(geometry, material);
        this.globe.castShadow = true;
        this.globe.receiveShadow = true;
        this.scene.add(this.globe);
    }

    drawEarthTexture(ctx, width, height) {
        // Base ocean color
        ctx.fillStyle = '#1e3a8a';
        ctx.fillRect(0, 0, width, height);

        // Draw continents with noise
        ctx.fillStyle = '#22c55e';
        
        // Simple continent shapes
        const continents = [
            // North America
            { x: 0.15, y: 0.3, w: 0.2, h: 0.25 },
            // South America  
            { x: 0.2, y: 0.55, w: 0.1, h: 0.3 },
            // Europe/Africa
            { x: 0.45, y: 0.25, w: 0.15, h: 0.5 },
            // Asia
            { x: 0.65, y: 0.2, w: 0.25, h: 0.35 },
            // Australia
            { x: 0.75, y: 0.65, w: 0.1, h: 0.08 }
        ];

        continents.forEach(continent => {
            const x = continent.x * width;
            const y = continent.y * height;
            const w = continent.w * width;
            const h = continent.h * height;
            
            // Draw irregular continent shape
            ctx.beginPath();
            for (let i = 0; i < 20; i++) {
                const angle = (i / 20) * Math.PI * 2;
                const noise = 0.8 + Math.random() * 0.4;
                const px = x + Math.cos(angle) * w * 0.5 * noise;
                const py = y + Math.sin(angle) * h * 0.5 * noise;
                
                if (i === 0) {
                    ctx.moveTo(px, py);
                } else {
                    ctx.lineTo(px, py);
                }
            }
            ctx.closePath();
            ctx.fill();
        });

        // Add some mountain ranges (darker green)
        ctx.fillStyle = '#16a34a';
        for (let i = 0; i < 50; i++) {
            const x = Math.random() * width;
            const y = Math.random() * height;
            const size = Math.random() * 10 + 2;
            
            ctx.beginPath();
            ctx.arc(x, y, size, 0, Math.PI * 2);
            ctx.fill();
        }

        // Add ice caps
        ctx.fillStyle = '#f0f9ff';
        // North pole
        ctx.beginPath();
        ctx.arc(width/2, 0, width * 0.1, 0, Math.PI * 2);
        ctx.fill();
        // South pole
        ctx.beginPath();
        ctx.arc(width/2, height, width * 0.08, 0, Math.PI * 2);
        ctx.fill();
    }

    createAtmosphere() {
        const geometry = new THREE.SphereGeometry(1.05, 64, 64);
        const material = new THREE.MeshBasicMaterial({
            color: 0x4488ff,
            transparent: true,
            opacity: 0.1,
            side: THREE.BackSide
        });

        this.atmosphere = new THREE.Mesh(geometry, material);
        this.scene.add(this.atmosphere);
    }

    addEventListeners() {
        // Handle window resize
        window.addEventListener('resize', () => this.onWindowResize());
        
        // Handle mouse interaction
        let mouseDown = false;
        let mouseX = 0;
        let mouseY = 0;

        this.canvas.addEventListener('mousedown', (event) => {
            mouseDown = true;
            mouseX = event.clientX;
            mouseY = event.clientY;
            this.isRotating = false;
        });

        this.canvas.addEventListener('mouseup', () => {
            mouseDown = false;
            setTimeout(() => {
                this.isRotating = true;
            }, 2000); // Resume rotation after 2 seconds
        });

        this.canvas.addEventListener('mousemove', (event) => {
            if (!mouseDown) return;

            const deltaX = event.clientX - mouseX;
            const deltaY = event.clientY - mouseY;

            this.globe.rotation.y += deltaX * 0.01;
            this.globe.rotation.x += deltaY * 0.01;

            mouseX = event.clientX;
            mouseY = event.clientY;
        });

        // Touch events for mobile
        this.canvas.addEventListener('touchstart', (event) => {
            event.preventDefault();
            const touch = event.touches[0];
            mouseDown = true;
            mouseX = touch.clientX;
            mouseY = touch.clientY;
            this.isRotating = false;
        });

        this.canvas.addEventListener('touchend', (event) => {
            event.preventDefault();
            mouseDown = false;
            setTimeout(() => {
                this.isRotating = true;
            }, 2000);
        });

        this.canvas.addEventListener('touchmove', (event) => {
            event.preventDefault();
            if (!mouseDown) return;

            const touch = event.touches[0];
            const deltaX = touch.clientX - mouseX;
            const deltaY = touch.clientY - mouseY;

            this.globe.rotation.y += deltaX * 0.01;
            this.globe.rotation.x += deltaY * 0.01;

            mouseX = touch.clientX;
            mouseY = touch.clientY;
        });
    }

    onWindowResize() {
        const width = this.canvas.clientWidth;
        const height = this.canvas.clientHeight;

        this.camera.aspect = width / height;
        this.camera.updateProjectionMatrix();
        this.renderer.setSize(width, height);
    }

    updateGlobeAppearance(probability) {
        this.currentProbability = probability;
        
        // Change globe color based on probability
        if (probability > 0.7) {
            // Success - golden glow
            this.atmosphere.material.color.setHex(0xffd700);
            this.atmosphere.material.opacity = 0.3;
        } else if (probability < 0.3) {
            // Failure - red glow
            this.atmosphere.material.color.setHex(0xff4444);
            this.atmosphere.material.opacity = 0.3;
        } else {
            // Neutral - blue glow
            this.atmosphere.material.color.setHex(0x4488ff);
            this.atmosphere.material.opacity = 0.1;
        }

        // Adjust rotation speed based on probability
        this.rotationSpeed = 0.003 + (probability * 0.004);
    }

    animate() {
        this.animationId = requestAnimationFrame(() => this.animate());

        // Rotate globe
        if (this.isRotating) {
            this.globe.rotation.y += this.rotationSpeed;
            this.atmosphere.rotation.y += this.rotationSpeed * 0.8;
        }

        // Slowly rotate stars
        this.stars.rotation.y += 0.0002;
        this.stars.rotation.x += 0.0001;

        // Pulse atmosphere based on probability
        const time = Date.now() * 0.001;
        const pulse = Math.sin(time * 2) * 0.05 + 1;
        this.atmosphere.scale.setScalar(pulse);

        // Render
        this.renderer.render(this.scene, this.camera);
    }

    destroy() {
        if (this.animationId) {
            cancelAnimationFrame(this.animationId);
        }
        
        // Clean up Three.js objects
        if (this.renderer) {
            this.renderer.dispose();
        }
        
        // Remove event listeners
        window.removeEventListener('resize', this.onWindowResize);
    }

    // Public methods for game interaction
    setRotationSpeed(speed) {
        this.rotationSpeed = speed;
    }

    pauseRotation() {
        this.isRotating = false;
    }

    resumeRotation() {
        this.isRotating = true;
    }

    triggerVictoryAnimation() {
        // Special animation for victory
        this.atmosphere.material.color.setHex(0xffd700);
        this.atmosphere.material.opacity = 0.5;
        
        // Increase rotation speed temporarily
        const originalSpeed = this.rotationSpeed;
        this.rotationSpeed = 0.02;
        
        setTimeout(() => {
            this.rotationSpeed = originalSpeed;
        }, 3000);
    }

    triggerDefeatAnimation() {
        // Special animation for defeat
        this.atmosphere.material.color.setHex(0xff4444);
        this.atmosphere.material.opacity = 0.4;
        
        // Slow down rotation
        const originalSpeed = this.rotationSpeed;
        this.rotationSpeed = 0.001;
        
        setTimeout(() => {
            this.rotationSpeed = originalSpeed;
        }, 3000);
    }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = Globe;
}
