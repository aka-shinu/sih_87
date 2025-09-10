"use client";
import React, { createContext, useContext } from "react";
import { ChevronLeft, ChevronRight, X } from "lucide-react";
import { cn } from "@/lib/utils";
import { AnimatePresence, motion } from "framer-motion";
import { CarouselProps, CarouselContextType, CardProps } from "@/types/carousel";
import { useCarousel } from "@/hooks/useCarousel";
import { useCardModal, useImageLoading } from "@/utils/carouselUtils";
import { ImageProps } from "@/types/image";

export const CarouselContext = createContext<CarouselContextType>({
  onCardClose: () => {},
  currentIndex: 0,
});

export const Carousel = ({ items, initialScroll = 0 }: CarouselProps) => {
  const {
    carouselRef,
    canScrollLeft,
    canScrollRight,
    checkScrollability,
    scrollLeft,
    scrollRight,
    handleCardClose
  } = useCarousel(initialScroll);

  return (
    <CarouselContext.Provider value={{ onCardClose: handleCardClose, currentIndex: 0 }}>
      <div className="relative w-full">
        <div
          className="flex w-full overflow-x-scroll overscroll-x-auto scroll-smooth py-10 [scrollbar-width:none] md:py-15"
          ref={carouselRef}
          onScroll={checkScrollability}
        >
          <div className={cn("absolute right-0 z-[1000] h-auto w-[5%] overflow-hidden bg-gradient-to-l")}></div>
          <div className={cn("flex flex-row justify-start gap-4", "mx-auto max-w-7xl")}>
            {items.map((item, index) => (
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.2 * index, ease: "easeOut" }}
                key={"card" + index}
                className="rounded-3xl last:pr-[5%] md:last:pr-[33%]"
              >
                {item}
              </motion.div>
            ))}
          </div>
        </div>
        {/* <div className="mr-10 flex justify-end gap-2">
          <button
            className="relative z-40 flex h-10 w-10 items-center justify-center rounded-full bg-gray-100 disabled:opacity-50"
            onClick={scrollLeft}
            disabled={!canScrollLeft}
          >
            <ChevronLeft className="h-6 w-6 text-gray-500" />
          </button>
          <button
            className="relative z-40 flex h-10 w-10 items-center justify-center rounded-full bg-gray-100 disabled:opacity-50"
            onClick={scrollRight}
            disabled={!canScrollRight}
          >
            <ChevronRight className="h-6 w-6 text-gray-500" />
          </button>
        </div> */}
      </div>
    </CarouselContext.Provider>
  );
};

export const Card = ({ card, index, layout = false, cardWidth, cardHeight }: CardProps) => {
  const { open, containerRef, handleOpen, handleClose } = useCardModal();
  const { onCardClose } = useContext(CarouselContext);

  const handleCardClose = () => {
    handleClose();
    onCardClose(index);
  };

  return (
    <>
      <AnimatePresence>
        {open && (
          <div className="fixed inset-0 z-50 h-screen overflow-auto">
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="fixed inset-0 h-full w-full bg-black/80 backdrop-blur-lg"
            />
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              ref={containerRef}
              layoutId={layout ? `card-${card.title}` : undefined}
              className="relative z-[60] mx-auto my-10 h-fit max-w-5xl rounded-3xl bg-white p-4 font-sans md:p-10 dark:bg-neutral-900"
            >
              <button
                className="sticky top-4 right-0 ml-auto flex h-8 w-8 items-center justify-center rounded-full bg-black dark:bg-white"
                onClick={handleCardClose}
              >
                <X className="h-6 w-6 text-neutral-100 dark:text-neutral-900" />
              </button>
               <motion.p
                 layoutId={layout ? `category-${card.title}` : undefined}
                 className="text-xs sm:text-sm md:text-base lg:text-lg font-medium text-black dark:text-white"
               >
                 {card.category}
               </motion.p>
               <motion.p
                 layoutId={layout ? `title-${card.title}` : undefined}
                 className="mt-1 sm:mt-2 md:mt-3 lg:mt-4 text-lg sm:text-xl md:text-2xl lg:text-3xl xl:text-4xl 2xl:text-5xl font-semibold text-neutral-700 dark:text-white leading-tight"
               >
                 {card.title}
               </motion.p>
              <div className="py-10">{card.content}</div>
            </motion.div>
          </div>
        )}
      </AnimatePresence>
      <motion.button
        layoutId={layout ? `card-${card.title}` : undefined}
        onClick={handleOpen}
        className={`relative z-10 flex flex-col items-start justify-start overflow-hidden rounded-3xl bg-gray-100 dark:bg-neutral-900 ${cardWidth || 'w-56 md:w-96'} ${cardHeight || 'h-80 md:h-[40rem]'}`}
      >
        <div className="pointer-events-none absolute inset-x-0 top-0 z-30 h-full bg-gradient-to-b from-black/50 via-transparent to-transparent" />
         <div className="relative z-40 p-2 sm:p-3 md:p-4 lg:p-6 xl:p-8 h-full flex flex-col">
           <motion.p
             layoutId={layout ? `category-${card.category}` : undefined}
             className="text-left font-sans text-[0.6rem] sm:text-[0.7rem] md:text-[0.8rem] lg:text-[0.9rem] xl:text-base font-medium text-white leading-tight"
           >
             {card.category}
           </motion.p>
           <motion.p
             layoutId={layout ? `title-${card.title}` : undefined}
             className="mt-0.5 sm:mt-1 md:mt-1.5 lg:mt-2 text-left font-sans text-[0.7rem] sm:text-[0.8rem] md:text-[0.9rem] lg:text-base xl:text-lg 2xl:text-xl font-semibold [text-wrap:balance] text-white leading-tight"
           >
             {card.title}
           </motion.p>
         </div>
        <BlurImage
          src={card.src}
          alt={card.title}
          fill
          className="absolute inset-0 z-10 object-cover"
        />
      </motion.button>
    </>
  );
};

export const BlurImage = ({ height, width, src, className, alt, ...rest }: ImageProps) => {
  const { isLoading, handleLoad } = useImageLoading();
  
  const imgProps = { ...rest };
  delete imgProps.fill;
  delete imgProps.blurDataURL;
  
  return (
    <img
      className={cn("h-full w-full transition duration-300", isLoading ? "blur-sm" : "blur-0", className)}
      onLoad={handleLoad}
      src={src as string}
      width={width}
      height={height}
      loading="lazy"
      decoding="async"
      alt={alt ? alt : "Background of a beautiful view"}
      {...imgProps}
    />
  );
};
