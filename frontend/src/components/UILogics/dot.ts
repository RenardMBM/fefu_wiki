export default class Dot {
    constructor(private rating: number, private size: number, private num: number) { }
    public draw(canvas: HTMLCanvasElement): void {
        // resize canvas to dot size
        const canvasDim = this.size;
        canvas.width = canvasDim;
        canvas.height = canvasDim;
        this.rating -= this.num - 1;
        if (this.rating > 1){
            this.rating = 1;
        }
        else if (this.rating < 0) {
            this.rating = 0;
        }

        const ctx = canvas.getContext('2d')!;
        ctx.fillStyle = '#ffaa2b';
        ctx.fillRect(0, 0, Math.floor(this.rating * this.size), this.size);

    }
}