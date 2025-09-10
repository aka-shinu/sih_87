import { ArrowRightIcon } from "@radix-ui/react-icons";
import { Button } from "@/components/ui/Button";
import { cn } from "@/lib/utils";
import { BentoGridProps, BentoCardProps } from "@/types/bento";
 
const BentoGrid = ({ children, className, ...props }: BentoGridProps) => (
  <div
    className={cn("flex w-full gap-3", className)}
    {...props}
  >
    {children}
  </div>
);
 
const BentoCard = ({ name, className, background, Icon, description, href, cta, ...props }: BentoCardProps) => (
  <div
    key={name}
    className={cn(
      "group relative flex flex-col justify-between overflow-hidden rounded-xl h-64",
      "bg-white border border-gray-200 shadow-lg hover:shadow-xl",
      "transform-gpu transition-all duration-300 hover:scale-[1.02]",
      className,
    )}
    {...props}
  >
    <div>{background}</div>
    <div className="p-3">
      <div className="pointer-events-none z-10 flex transform-gpu flex-col gap-1 transition-all duration-300 lg:group-hover:-translate-y-10">
        <Icon className="h-8 w-8 origin-left transform-gpu text-gray-600 transition-all duration-300 ease-in-out group-hover:scale-75" />
        <h3 className="text-lg font-semibold text-gray-900">{name}</h3>
        <p className="max-w-lg text-sm text-gray-600">{description}</p>
      </div>
      <div className="lg:hidden pointer-events-none flex w-full translate-y-0 transform-gpu flex-row items-center transition-all duration-300 group-hover:translate-y-0 group-hover:opacity-100">
        <Button variant="link" asChild size="sm" className="pointer-events-auto p-0">
          <a href={href}>
            {cta}
            <ArrowRightIcon className="ms-2 h-4 w-4 rtl:rotate-180" />
          </a>
        </Button>
      </div>
    </div>
    <div className="hidden lg:flex pointer-events-none absolute bottom-0 w-full translate-y-10 transform-gpu flex-row items-center p-4 opacity-0 transition-all duration-300 group-hover:translate-y-0 group-hover:opacity-100">
      <Button variant="link" asChild size="sm" className="pointer-events-auto p-0">
        <a href={href}>
          {cta}
          <ArrowRightIcon className="ms-2 h-4 w-4 rtl:rotate-180" />
        </a>
      </Button>
    </div>
    <div className="pointer-events-none absolute inset-0 transform-gpu transition-all duration-300 group-hover:bg-black/[.03] group-hover:dark:bg-neutral-800/10" />
  </div>
);
 
export { BentoCard, BentoGrid };